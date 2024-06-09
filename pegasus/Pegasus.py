import requests
import markdownify
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re
import loguru
import time
from art import *
from litellm import completion
from tqdm import tqdm
import litellm
# litellm.set_verbose=True

logger = loguru.logger

class Pegasus:
    def __init__(self, output_dir, exclude_selectors=None, include_domain=None, exclude_keywords=None, output_extension=".md", 
                 dust_size=1000, max_depth=None, system_message=None, classification_prompt=None, max_retries=3, 
                 model='gemini/gemini-1.5-pro-latest', rate_limit_sleep=60, other_error_sleep=10):
        self.output_dir = output_dir
        self.exclude_selectors = exclude_selectors
        self.include_domain = include_domain
        self.exclude_keywords = exclude_keywords
        self.visited_urls = set()
        self.output_extension = output_extension
        self.dust_size = dust_size
        self.max_depth = max_depth
        self.domain_summaries = {}
        self.system_message = system_message
        self.classification_prompt = classification_prompt
        self.max_retries = max_retries
        self.model = model
        self.rate_limit_sleep = rate_limit_sleep
        self.other_error_sleep = other_error_sleep
        tprint("  Pegasus  ", font="rnd-xlarge")
        logger.info("初期化パラメータ:")
        logger.info(f"  output_dir: {output_dir}")
        logger.info(f"  exclude_selectors: {exclude_selectors}")
        logger.info(f"  include_domain: {include_domain}")
        logger.info(f"  exclude_keywords: {exclude_keywords}")
        logger.info(f"  output_extension: {output_extension}")
        logger.info(f"  dust_size: {dust_size}")
        logger.info(f"  max_depth: {max_depth}")
        logger.info(f"  system_message: {system_message}")
        logger.info(f"  classification_prompt: {classification_prompt}")
        logger.info(f"  max_retries: {max_retries}")
        logger.info(f"  model: {model}")
        logger.info(f"  rate_limit_sleep: {rate_limit_sleep}")
        logger.info(f"  other_error_sleep: {other_error_sleep}")

    def filter_site(self, markdown_content):
        if(self.classification_prompt is None):
            return True
        
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                messages = [
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": f"{self.classification_prompt}\n\n{markdown_content}"}
                ]
                response = completion(
                    model="gemini/gemini-1.5-pro-latest", 
                    messages=messages
                )
                content = response.get('choices', [{}])[0].get('message', {}).get('content')
                logger.debug(f"content : {content}")
                if "true" in content.lower():
                    return True
                elif "false" in content.lower():
                    return False
                else:
                    raise ValueError("分類結果が曖昧です。")
            except Exception as e:
                retry_count += 1
                logger.warning(f"フィルタリングでエラーが発生しました。リトライします。（{retry_count}/{self.max_retries}）\nError: {e}")
                
                if "429" in str(e):
                    sleep_time = self.rate_limit_sleep  # レート制限エラー時のスリープ時間をself.rate_limit_sleepから取得
                else:
                    sleep_time = self.other_error_sleep  # その他のエラー時のスリープ時間をself.other_error_sleepから取得
                
                for _ in tqdm(range(sleep_time), desc="Sleeping", unit="s"):
                    time.sleep(1)
        
        logger.error(f"フィルタリングに失敗しました。リトライ回数の上限に達しました。（{self.max_retries}回）")
        return True
    
    def download_and_convert(self, url, depth=0):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            if self.exclude_selectors:
                for selector in self.exclude_selectors:
                    for element in soup.select(selector):
                        element.decompose()

            markdown_content = markdownify.markdownify(str(soup))
            markdown_content = re.sub(r'\n{5,}', '\n\n\n\n', markdown_content)

            if not self.filter_site(markdown_content):
                parsed_url = urlparse(url)
                domain = parsed_url.netloc
                domain_dir = os.path.join(self.output_dir, domain)
                os.makedirs(domain_dir, exist_ok=True)
                excluded_dir = os.path.join(domain_dir, "excluded")
                os.makedirs(excluded_dir, exist_ok=True)
                output_file = f"{excluded_dir}/{parsed_url.path.replace('/', '_')}{self.output_extension}"
            else:
                parsed_url = urlparse(url)
                domain = parsed_url.netloc
                domain_dir = os.path.join(self.output_dir, domain)
                os.makedirs(domain_dir, exist_ok=True)

                output_file = f"{domain_dir}/{parsed_url.path.replace('/', '_')}{self.output_extension}"
                
                if len(markdown_content) < self.dust_size:
                    dust_dir = os.path.join(domain_dir, "dust")
                    os.makedirs(dust_dir, exist_ok=True)
                    output_file = f"{dust_dir}/{parsed_url.path.replace('/', '_')}{self.output_extension}"

                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(markdown_content)

                logger.info(f"[{depth}]変換成功: {url} ---> {output_file} [{len(markdown_content)/1000}kb]")

                if domain not in self.domain_summaries:
                    self.domain_summaries[domain] = []
                self.domain_summaries[domain].append(f"# {os.path.basename(output_file)}\n\n---\n\n{markdown_content}")

            if self.max_depth is None or depth < self.max_depth:
                soup_url = BeautifulSoup(response.text, 'html.parser')

                for link in soup_url.find_all('a'):
                    href = link.get('href')
                    if href:
                        absolute_url = urljoin(url, href)
                        if (self.include_domain and self.include_domain in absolute_url) or (self.include_domain == ""):
                            if self.exclude_keywords:
                                if any(keyword in absolute_url for keyword in self.exclude_keywords):
                                    continue
                            absolute_url = absolute_url.split('#')[0]
                            self.download_and_convert(absolute_url, depth + 1)

        except requests.exceptions.RequestException as e:
            logger.error(f"ダウンロードエラー: {url}: {e}")
        except IOError as e:
            logger.error(f"書き込みエラー: {output_file}: {e}")

    def create_domain_summaries(self):
        for domain, summaries in self.domain_summaries.items():
            summary_file = os.path.join(self.output_dir, f"{domain}_summary{self.output_extension}")
            with open(summary_file, 'w', encoding='utf-8') as file:
                file.write('\n\n'.join(summaries))
            logger.info(f"サマリーファイル作成: {summary_file}")

    def run(self, base_url):
        logger.info(f"スクレイピング開始: base_url={base_url}")
        self.download_and_convert(base_url)
        self.create_domain_summaries()
        logger.info("スクレイピング完了")
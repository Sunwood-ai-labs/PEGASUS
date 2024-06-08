# pegasus/pegasus.py
import requests
import markdownify
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re
import loguru
from art import *

logger = loguru.logger

class Pegasus:
   def __init__(self, base_url, output_dir, exclude_selectors=None, include_domain=None, exclude_keywords=None, output_extension=".md", dust_size=1000):
       self.base_url = base_url
       self.output_dir = output_dir
       self.exclude_selectors = exclude_selectors
       self.include_domain = include_domain
       self.exclude_keywords = exclude_keywords
       self.visited_urls = set()
       self.output_extension = output_extension
       self.dust_size = dust_size
       tprint("  Pegasus  ", font="rnd-xlarge")
       logger.info("初期化パラメータ:")
       logger.info(f"  base_url: {base_url}")
       logger.info(f"  output_dir: {output_dir}")
       logger.info(f"  exclude_selectors: {exclude_selectors}")
       logger.info(f"  include_domain: {include_domain}")
       logger.info(f"  exclude_keywords: {exclude_keywords}")
       logger.info(f"  output_extension: {output_extension}")
       logger.info(f"  dust_size: {dust_size}")
       
   def download_and_convert(self, url):
       os.makedirs(self.output_dir, exist_ok=True)
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

           parsed_url = urlparse(url)
           output_file = f"{self.output_dir}/{parsed_url.path.replace('/', '_')}{self.output_extension}"
           
           if len(markdown_content) < self.dust_size:
               dust_dir = os.path.join(self.output_dir, "dust")
               os.makedirs(dust_dir, exist_ok=True)
               output_file = f"{dust_dir}/{parsed_url.path.replace('/', '_')}{self.output_extension}"

           with open(output_file, 'w', encoding='utf-8') as file:
               file.write(markdown_content)

           logger.info(f"変換成功: {url} ---> {output_file} [{len(markdown_content)/1000}kb]")

           soup_url = BeautifulSoup(response.text, 'html.parser')

           for link in soup_url.find_all('a'):
               href = link.get('href')
               if href:
                   absolute_url = urljoin(url, href)
                   if self.include_domain and self.include_domain in absolute_url:
                       if self.exclude_keywords:
                           if any(keyword in absolute_url for keyword in self.exclude_keywords):
                               continue
                       absolute_url = absolute_url.split('#')[0]
                       self.download_and_convert(absolute_url)

       except requests.exceptions.RequestException as e:
           logger.error(f"ダウンロードエラー: {url}: {e}")
       except IOError as e:
           logger.error(f"書き込みエラー: {output_file}: {e}")

   def run(self):
       logger.info(f"スクレイピング開始: base_url={self.base_url}")
       self.download_and_convert(self.base_url)
       logger.info("スクレイピング完了")
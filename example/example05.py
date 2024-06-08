import requests
import markdownify
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re

def download_and_convert(url, output_dir, visited_urls, exclude_selectors=None, include_domain=None, exclude_keywords=None):
    os.makedirs(output_dir, exist_ok=True)    
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        # URLからWebページをダウンロード
        response = requests.get(url)
        response.raise_for_status()

        # BeautifulSoupオブジェクトを作成
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 除外するセレクターに一致する要素を削除
        if exclude_selectors:
            for selector in exclude_selectors:
                for element in soup.select(selector):
                    element.decompose()

        # HTMLをマークダウンに変換
        markdown_content = markdownify.markdownify(str(soup))

        # 5行以上の連続した空行を削除
        markdown_content = re.sub(r'\n{5,}', '\n\n\n\n', markdown_content)

        # マークダウンをファイルに保存
        parsed_url = urlparse(url)
        output_file = f"{output_dir}/{parsed_url.path.replace('/', '_')}.md"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        print(f"Successfully converted {url} ---> {output_file}")

        # BeautifulSoupオブジェクトを作成
        soup_url = BeautifulSoup(response.text, 'html.parser')
        
        # ページ内のリンクを探索
        for link in soup_url.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                if include_domain and include_domain in absolute_url:
                    if exclude_keywords:
                        if any(keyword in absolute_url for keyword in exclude_keywords):
                            continue
                    # URLのフラグメント部分を除去
                    absolute_url = absolute_url.split('#')[0]
                    download_and_convert(absolute_url, output_dir, visited_urls, exclude_selectors, include_domain, exclude_keywords)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

# 使用例
base_url = "https://docs.eraser.io/docs/what-is-eraser"
output_dir = "eraser_docs"
visited_urls = set()
exclude_selectors = [
    'header',
    'footer',
    'nav',
    'aside',
    '.sidebar',
    '.header',
    '.footer',
    '.navigation',
    '.breadcrumbs'
]
include_domain = "docs.eraser.io"
exclude_keywords = ["login"]

download_and_convert(base_url, output_dir, visited_urls, exclude_selectors, include_domain, exclude_keywords)
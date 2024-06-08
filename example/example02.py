import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_and_convert(url, output_dir, visited_urls):
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        # URLからWebページをダウンロード
        response = requests.get(url)
        response.raise_for_status()

        # HTMLをマークダウンに変換
        h = html2text.HTML2Text()
        h.ignore_links = True
        markdown_content = h.handle(response.text)

        # マークダウンをファイルに保存
        parsed_url = urlparse(url)
        output_file = f"{output_dir}/{parsed_url.path.replace('/', '_')}.md"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        print(f"Successfully converted {url} to {output_file}")

        # ページ内のリンクを探索
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                if "docs.eraser.io" in absolute_url:
                    # docs.eraser.ioを含むURLのみ探索
                    # URLのフラグメント部分を除去
                    absolute_url = absolute_url.split('#')[0]
                    download_and_convert(absolute_url, output_dir, visited_urls)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

# 使用例
base_url = "https://docs.eraser.io/docs/what-is-eraser"
output_dir = "eraser_docs"
visited_urls = set()
download_and_convert(base_url, output_dir, visited_urls)
import requests
import markdownify

def download_and_convert(url, output_file):
    try:
        # URLからWebページをダウンロード
        response = requests.get(url)
        response.raise_for_status()

        # HTMLをマークダウンに変換
        markdown_content = markdownify.markdownify(response.text)

        # マークダウンをファイルに保存
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        print(f"Successfully converted {url} to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

# 使用例
url = "https://docs.eraser.io/docs/examples-4"
output_file = "example.md"
download_and_convert(url, output_file)
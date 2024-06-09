import argparse
from .Pegasus import Pegasus
from dotenv import load_dotenv
load_dotenv(verbose=True)

def main():
    parser = argparse.ArgumentParser(description='Pegasus')
    parser.add_argument('--base-url', help='スクレイピングを開始するベースURL')
    parser.add_argument('--url-file', help='スクレイピングするURLが記載されたテキストファイル')
    parser.add_argument('output_dir', help='Markdownファイルの出力ディレクトリ')
    parser.add_argument('--exclude-selectors', nargs='+', help='除外するCSSセレクター')
    parser.add_argument('--include-domain', default='', help='URLマッチングに含めるドメイン')
    parser.add_argument('--exclude-keywords', nargs='+', help='URLマッチングから除外するキーワード')
    parser.add_argument('--output-extension', default='.md', help='出力ファイルの拡張子 (デフォルト: .md)')
    parser.add_argument('--dust-size', type=int, default=1000, help='ダストフォルダに移動するファイルサイズのしきい値 (デフォルト: 1000バイト)')
    parser.add_argument('--max-depth', type=int, default=None, help='再帰処理の最大深度 (デフォルト: 制限なし)')
    parser.add_argument('--system-message', default=None, help='LiteLLMのシステムメッセージ（サイトの分類に使用）')
    parser.add_argument('--classification-prompt', default=None, help='LiteLLMのサイト分類プロンプト（TrueまたはFalseを返すようにしてください）')
    parser.add_argument('--max-retries', type=int, default=3, help='フィルタリングのリトライ回数の上限（デフォルト：3）')
    parser.add_argument('--model', default='gemini/gemini-1.5-pro-latest', help='LiteLLMのモデル名 (デフォルト: gemini/gemini-1.5-pro-latest)')
    parser.add_argument('--rate-limit-sleep', type=int, default=60, help='レート制限エラー時のスリープ時間（秒） (デフォルト: 60)')
    parser.add_argument('--other-error-sleep', type=int, default=10, help='その他のエラー時のスリープ時間（秒） (デフォルト: 10)')
    
    args = parser.parse_args()

    pegasus = Pegasus(
        output_dir=args.output_dir,
        exclude_selectors=args.exclude_selectors,
        include_domain=args.include_domain,
        exclude_keywords=args.exclude_keywords,
        output_extension=args.output_extension,
        dust_size=args.dust_size,
        max_depth=args.max_depth,
        system_message=args.system_message,
        classification_prompt=args.classification_prompt,
        max_retries=args.max_retries
    )

    if args.base_url:
        pegasus.run(args.base_url)
    elif args.url_file:
        with open(args.url_file, 'r') as file:
            urls = file.read().splitlines()
            for url in urls:
                pegasus.run(url)
    else:
        parser.error("--base-url または --url-file のいずれかを指定してください。")

if __name__ == '__main__':
    main()
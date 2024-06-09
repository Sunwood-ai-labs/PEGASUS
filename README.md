<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/PEGASUS.jpeg" width="100%">
<br>
<h1 align="center">P.E.G.A.S.U.S</h1>
<h2 align="center">
  ～ Parsing Extracting Generating Automated Scraping Utility System ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/PEGASUS-SURF">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/PEGASUS-SURF">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/PEGASUS-SURF">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/PEGASUS-SURF">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/PEGASUS-SURF">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/PEGASUS-SURF">
<a href="https://github.com/Sunwood-ai-labs/PEGASUS" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=PEGASUS&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/PEGASUS">
<a href="https://github.com/Sunwood-ai-labs/PEGASUS"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/PEGASUS/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/PEGASUS"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/PEGASUS"></a>
<a href="https://github.com/Sunwood-ai-labs/PEGASUS"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/PEGASUS"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/PEGASUS?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/PEGASUS?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/PEGASUS/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/tag/pegasus/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。


こんにちは！PEGASUSへようこそ！PEGASUSは、ウェブサイトを再帰的にクロールし、そのコンテンツを美しいMarkdown形式に変換するパワフルで柔軟なPythonパッケージです。

PEGASUSを使えば、指定したURLから始まり、リンクをたどって関連するページを探索し、HTMLコンテンツを見やすいMarkdownドキュメントに変換することができます。コマンドラインインターフェイス（CLI）から実行することも、Pythonスクリプトから直接使用することもできるので、とっても便利なんです！

## 🚀 インストール

pipを使ってPEGASUSをインストールしましょう。以下のコマンドを実行するだけです！👇

```shell
pip install pegasus-surf 
```

## 🎮 使い方

### 🖥️ コマンドラインから

PEGASUSをコマンドラインから使用するには、以下のようなコマンドを実行します。

```shell
# 単一のURLからスクレイピングを開始 🌐
pegasus --base-url https://example.com/start-page output_directory --exclude-selectors header footer nav --include-domain example.com --exclude-keywords login --output-extension txt

# 探索深度を指定して実行 🔍
pegasus  --base-url  https://docs.eraser.io/docs/what-is-eraser output/eraser_docs2 --exclude-selectors header footer nav aside .sidebar .header .footer .navigation .breadcrumbs --include-domain docs.eraser.io --exclude-keywords login --output-extension .txt --max-depth 2

# URLリストが記載されたテキストファイルからスクレイピングを開始 📜
pegasus --url-file urls.txt output/roomba --exclude-selectors header footer nav aside .sidebar .header .footer .navigation .breadcrumbs --exclude-keywords login --output-extension .txt --max-depth 1

# LLMを使用したサイトの分類を行いながらスクレイピング 🧠
pegasus --url-file urls.txt output/roomba2 --exclude-selectors header footer nav aside .sidebar .header .footer .navigation .breadcrumbs --exclude-keywords login --output-extension .txt --max-depth 1 --system-message "あなたは、与えられたウェブサイトのコンテンツが特定のトピックに関連する有用な情報を含んでいるかどうかを判断するアシスタントです。トピックに関連する有益な情報が含まれている場合は「True」、そうでない場合は「False」と回答してください。" --classification-prompt "次のウェブサイトのコンテンツは、Roomba APIやiRobotに関する有益な情報を提供していますか？ 提供している場合は「True」、そうでない場合は「False」と回答してください。"
```

オプションの意味はこんな感じです！👀

- `--base-url`: スクレイピングを開始するベースURLを指定します。
- `--url-file`: スクレイピングするURLが記載されたテキストファイルを指定します。
- `--output-extension`: 出力ファイルの拡張子を指定します（デフォルト: .md）。
- `--dust-size`: ダストフォルダに移動するファイルサイズのしきい値をバイト単位で指定します（デフォルト: 1000）。
- `--max-depth`: 再帰処理の最大深度を指定します（デフォルト: 制限なし）。
- `--system-message`: LLMのシステムメッセージを指定します（サイトの分類に使用）。
- `--classification-prompt`: LLMのサイト分類プロンプトを指定します。TrueまたはFalseを返すようにしてください。
- `--max-retries`: フィルタリングのリトライ回数の上限を指定します（デフォルト: 3）。
- `--model`: LLMのモデル名を指定します（デフォルト: gemini/gemini-1.5-pro-latest）。
- `--rate-limit-sleep`: レート制限エラー時のスリープ時間を秒単位で指定します（デフォルト: 60）。
- `--other-error-sleep`: その他のエラー時のスリープ時間を秒単位で指定します（デフォルト: 10）。

### 🐍 PythonスクリプトからPEGASUSを使う

PEGASUSをPythonスクリプトから使用するには、以下のようなコードを書きます。

```python
from pegasus import Pegasus

pegasus = Pegasus(
    output_dir="output_directory", 
    exclude_selectors=['header', 'footer', 'nav'],
    include_domain="example.com",
    exclude_keywords=["login"],
    output_extension=".txt",
    dust_size=500,
    max_depth=2,
    system_message="You are an assistant to determine if the content of a given website contains useful information related to a specific topic. If it contains relevant and beneficial information about the topic, answer 'True', otherwise answer 'False'.",
    classification_prompt="Does the content of the following website provide beneficial information about the Roomba API or iRobot? If so, answer 'True', if not, answer 'False'.",
    max_retries=5,
    model="gemini/gemini-1.5-pro-latest",
    rate_limit_sleep=30,
    other_error_sleep=5
)
pegasus.run("https://example.com/start-page")
```

パラメータの意味はこちらです！

- `output_dir`: Markdownファイルを保存するディレクトリを指定します。
- `exclude_selectors`: 除外するCSSセレクターのリストを指定します（オプション）。
- `include_domain`: クロールを特定のドメインに限定します（オプション）。
- `exclude_keywords`: URLに含まれる場合にページを除外するキーワードのリストを指定します（オプション）。
- `output_extension`: 出力ファイルの拡張子を指定します（デフォルト: .md）。
- `dust_size`: ダストフォルダに移動するファイルサイズのしきい値をバイト単位で指定します（デフォルト: 1000）。
- `max_depth`: 再帰処理の最大深度を指定します（デフォルト: 制限なし）。
- `system_message`: LLMのシステムメッセージを指定します（サイトの分類に使用）。
- `classification_prompt`: LLMのサイト分類プロンプトを指定します。TrueまたはFalseを返すようにしてください。
- `max_retries`: フィルタリングのリトライ回数の上限を指定します（デフォルト: 3）。
- `model`: LLMのモデル名を指定します（デフォルト: gemini/gemini-1.5-pro-latest）。
- `rate_limit_sleep`: レート制限エラー時のスリープ時間を秒単位で指定します（デフォルト: 60）。
- `other_error_sleep`: その他のエラー時のスリープ時間を秒単位で指定します（デフォルト: 10）。

## ✨ PEGASUSの特長

- 指定したURLから始まり、リンクを再帰的にたどってウェブサイトを探索します。🔍
- HTMLコンテンツを美しくフォーマットされたMarkdownに変換します。📝
- 柔軟な設定オプションにより、クロールと変換のプロセスをカスタマイズできます。⚙️
- ヘッダー、フッター、ナビゲーションなどの不要な要素を除外できます。🙅‍♀️
- 特定のドメインのみをクロールするように制限できます。🌐
- 特定のキーワードを含むURLを除外できます。🚫
- URLリストを記載したテキストファイルを指定してスクレイピングできます。📜
- LLMを使ってスクレイピングしたサイトを分類できます。🧠

## ⚠️ 注意事項

- PEGASUSは、適切な使用方法とウェブサイトの利用規約に従ってご利用ください。🙏
- 過度なリクエストを送信しないよう、適切な遅延を設けてください。⏰

## 📜 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。

## 開発者用

### パッケージの構成

[View on Eraser![](https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0/preview?elements=ooYqYlIqai8z1hvLott86w&type=embed)](https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0?elements=ooYqYlIqai8z1hvLott86w)

### パッケージのフローチャート

<p align="center">
<a href="https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0?elements=GXyvnJ89wCRZwFdm00Zbmg">View on Eraser<br /><img src="https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0/preview?elements=GXyvnJ89wCRZwFdm00Zbmg&type=embed"  width="50%"/></a>
</p>

### パッケージのER図

[View on Eraser![](https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0/preview?elements=KStkmTRUuZ5AiJNPC8E40g&type=embed)](https://app.eraser.io/workspace/8cnaevNcF1kxMsfSfGl0?elements=KStkmTRUuZ5AiJNPC8E40g)


## 🤝 貢献

プルリクエストや改善案は大歓迎です！🎉 バグ報告や機能リクエストがある場合は、issueを作成してください。😊

---

PEGASUSを使用すれば、ウェブサイトを再帰的に探索し、コンテンツを美しいMarkdownドキュメントに変換できます。📜✨ ドキュメンテーションの自動化、コンテンツの管理、データ分析などにぜひお役立てください！🙌
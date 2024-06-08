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
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。


pegasus は、ウェブサイトを再帰的にクロールし、そのコンテンツを Markdown 形式に変換するパワフルで柔軟な Python パッケージです。指定した URL から始まり、リンクをたどって関連するページを探索し、HTML コンテンツを美しい Markdown ドキュメントに変換します。コマンドラインインターフェイス (CLI) から実行することも、Python スクリプトから直接使用することもできます。

## インストール

pip を使用して pegasus をインストールします。

```shell
pip install pegasus
```

## 使い方

### コマンドラインから

pegasus をコマンドラインから使用するには、以下のようなコマンドを実行します。

```shell
pegasus https://example.com/start-page output_directory --exclude-selectors header footer nav --include-domain example.com --exclude-keywords login --output-extension txt
pegasus  https://docs.eraser.io/docs/what-is-eraser output/eraser_docs --exclude-selectors header footer nav aside .sidebar .header .footer .navigation .breadcrumbs --include-domain docs.eraser.io --exclude-keywords login --output-extension .txt
```

- `https://example.com/start-page`: クロールを開始するベース URL を指定します。
- `output_directory`: Markdown ファイルを保存するディレクトリを指定します。
- `--exclude-selectors`: 除外する CSS セレクターをスペース区切りで指定します（オプション）。
- `--include-domain`: クロールを特定のドメインに限定します（オプション）。
- `--exclude-keywords`: URL に含まれる場合にページを除外するキーワードをスペース区切りで指定します（オプション）。

### Python スクリプトから

pegasus を Python スクリプトから使用するには、以下のようなコードを書きます。

```python
from pegasus import pegasus

pegasus = pegasus(
    base_url="https://example.com/start-page",
    output_dir="output_directory",
    exclude_selectors=['header', 'footer', 'nav'],
    include_domain="example.com",
    exclude_keywords=["login"]
)
pegasus.run()
```

- `base_url`: クロールを開始するベース URL を指定します。
- `output_dir`: Markdown ファイルを保存するディレクトリを指定します。
- `exclude_selectors`: 除外する CSS セレクターのリストを指定します（オプション）。
- `include_domain`: クロールを特定のドメインに限定します（オプション）。
- `exclude_keywords`: URL に含まれる場合にページを除外するキーワードのリストを指定します（オプション）。

## 特長

- 指定した URL から始まり、リンクを再帰的にたどってウェブサイトを探索します。
- HTML コンテンツを美しくフォーマットされた Markdown に変換します。
- 柔軟な設定オプションにより、クロールと変換のプロセスをカスタマイズできます。
- ヘッダー、フッター、ナビゲーションなどの不要な要素を除外できます。
- 特定のドメインのみをクロールするように制限できます。
- 特定のキーワードを含む URL を除外できます。

## 注意事項

- pegasus は、適切な使用方法とウェブサイトの利用規約に従ってご利用ください。
- 過度なリクエストを送信しないよう、適切な遅延を設けてください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

## 貢献

プルリクエストや改善案は大歓迎です。バグ報告や機能リクエストがある場合は、issue を作成してください。

---

pegasus を使用すれば、ウェブサイトを再帰的に探索し、コンテンツを美しい Markdown ドキュメントに変換できます。ドキュメンテーションの自動化、コンテンツの管理、データ分析などにぜひお役立てください！
<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/PEGASUS.jpeg" width="100%">
<br>
<h1 align="center">PEGASUS</h1>
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

## 🌟 イントロダクション

**Pegasus** は、ウェブサイトを再帰的にクロールし、そのコンテンツを美しくフォーマットされた Markdown ドキュメントに変換する、パワフルで柔軟な Python パッケージです。指定された URL から始まり、リンクをたどって関連するページを探索し、HTML コンテンツを構造化された Markdown ファイルに変換します。コマンドラインインターフェイス（CLI）から実行することも、Python スクリプトから直接使用することもできます。

## 🎥 デモ

*デモ動画は現在準備中です。*

## 🚀 はじめに

このリポジトリには、Pegasus を Docker Compose で簡単に実行するための設定ファイルが含まれています。

### 前提条件

* Docker
* Docker Compose

### 実行方法

1. リポジトリをクローンします。

```bash
git clone https://github.com/[あなたのユーザー名]/pegasus-docker-compose.git
```

2. ディレクトリに移動します。

```bash
cd pegasus-docker-compose
```

3. `.env` ファイルを編集し、`TARGET_URL` をクロールしたいウェブサイトの URL に設定します。

4. Docker Compose を起動します。

```bash
docker-compose up -d
```

5. プロセスが完了すると、Markdown ファイルが `output` ディレクトリに出力されます。

### オプション

`.env` ファイルで以下の環境変数を設定することで、Pegasus の動作をカスタマイズできます。

* `TARGET_URL`: クロールするウェブサイトの URL (必須)
* `OUTPUT_DIRECTORY`: Markdown ファイルを出力するディレクトリ (デフォルト: `./output`)
* `DEPTH`: クロールする深さ (デフォルト: `-1` (無制限))
* `LOG_LEVEL`: ログレベル (デフォルト: `INFO`)

### 例

`https://www.example.com` をクロールし、Markdown ファイルを `./my-output` ディレクトリに出力する例:

```
TARGET_URL=https://www.example.com
OUTPUT_DIRECTORY=./my-output
```

### 注意

* Pegasus は、ウェブサイトの構造やコンテンツによっては、期待通りの結果を得られない場合があります。
* 大規模なウェブサイトをクロールする場合は、時間とリソースの使用量に注意してください。
* クロールする前に、ウェブサイトの利用規約を確認してください。

## 📝 更新情報

*最新情報については、CHANGELOG.md ファイルを参照してください。*

## 🤝 コントリビューション

*コントリビューションは大歓迎です！*

## 📄 ライセンス

*このプロジェクトは、[ライセンス名] ライセンスの下でライセンスされています。*

## 🙏 謝辞

*Pegasus の開発に貢献してくれたすべての人に感謝します。*


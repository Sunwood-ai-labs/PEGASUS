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

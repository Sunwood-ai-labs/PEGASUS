## Pegasus: ウェブサイトをMarkdownに

Pegasusは、ウェブサイトを再帰的にクロールし、そのコンテンツを美しくフォーマットされたMarkdownドキュメントに変換する、パワフルで柔軟なPythonパッケージです。指定されたURLから始まり、リンクをたどって関連するページを探索し、HTMLコンテンツを構造化されたMarkdownファイルに変換します。コマンドラインインターフェイス（CLI）から実行することも、Pythonスクリプトから直接使用することもできます。

### Docker Compose を利用した実行

このリポジトリには、PegasusをDocker Composeで簡単に実行するための設定ファイルが含まれています。

#### 前提条件

* Docker
* Docker Compose

#### 実行方法

1. リポジトリをクローンします。

```
git clone https://github.com/[あなたのユーザー名]/pegasus-docker-compose.git
```

2. ディレクトリに移動します。

```
cd pegasus-docker-compose
```

3. `.env` ファイルを編集し、`TARGET_URL` をクロールしたいウェブサイトのURLに設定します。

4. Docker Compose を起動します。

```
docker-compose up -d
```

5. プロセスが完了すると、Markdownファイルが `output` ディレクトリに出力されます。

#### オプション

`.env` ファイルで以下の環境変数を設定することで、Pegasusの動作をカスタマイズできます。

* `TARGET_URL`: クロールするウェブサイトのURL (必須)
* `OUTPUT_DIRECTORY`: Markdownファイルを出力するディレクトリ (デフォルト: `./output`)
* `DEPTH`: クロールする深さ (デフォルト: `-1` (無制限))
* `LOG_LEVEL`: ログレベル (デフォルト: `INFO`)

#### 例

`https://www.example.com` をクロールし、Markdownファイルを `./my-output` ディレクトリに出力する例:

```
TARGET_URL=https://www.example.com
OUTPUT_DIRECTORY=./my-output
```

#### 注意

* Pegasusは、ウェブサイトの構造やコンテンツによっては、期待通りの結果を得られない場合があります。
* 大規模なウェブサイトをクロールする場合は、時間とリソースの使用量に注意してください。
* クロールする前に、ウェブサイトの利用規約を確認してください。
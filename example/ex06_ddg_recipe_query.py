from duckduckgo_search import DDGS
import json

# クエリ
with DDGS() as ddgs:
    results = list(ddgs.text(
        keywords='お好み焼き レシピ',      # 検索ワード
        region='jp-jp',       # リージョン 日本は"jp-jp",指定なしの場合は"wt-wt"
        safesearch='off',     # セーフサーチOFF->"off",ON->"on",標準->"moderate"
        timelimit=None,       # 期間指定 指定なし->None,過去1日->"d",過去1週間->"w",
                              # 過去1か月->"m",過去1年->"y"
        max_results=4         # 取得件数
    ))

# レスポンスの表示
for line in results:
    print(json.dumps(
        line,
        indent=2,
        ensure_ascii=False
    ))
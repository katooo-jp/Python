'''Webスクレイピング'''
'''
！！！スクレイピング時の注意事項！！！
1.サイトによっては禁止をしているので規約をよく読む。大体サイトのフッター部に規約のリンクあり。
2.連続して同じサイトから情報取得時は一秒以上時間を置く。サイトへの負担軽減のため
'''


'''requests'''
import requests
import time
# 連続で取得する場合は処理間にsleep()を利用
# time.sleep(1)


url = '対象のURL'

# HTTPリクエストを送信してHTMLを取得し、2行目で文字化け対策
response = requests.get(url)
response.encoding = response.apparent_encoding

'''
今回は下記htmlを取得できたと仮定。

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>解析用のHTML</title>
  </head>
  <body>
    <h1>解析用のHTML</h1>
    <ul id="link-list">
      <li>
        <a href="http://example.com/1">テスト1</a>
      </li>
      <li>
        <a href="http://example.com/2">テスト2</a>
      </li>
      <li>
        <a href="http://example.com/3">テスト3</a>
      </li>
    <ul>
  </body>
</html>
'''

'''BeatuifulSoup'''
'''
BeatuifulSoupはHTMLの解析に利用する
find()とfind_all()で要素の抽出
findメソッドは単一の値を返し値が見つからない場合はNoneを返す。
find_allは常にリストを返して値がない場合は空のリストを返す。
'''
from bs4 import BeautifulSoup

#　BeatuifulSoupにHTMLを渡す
bs = BeautifulSoup(response.text, 'html.parser')

# ulタグで囲まれた部分を抽出します
ul_tag = bs.find('ul')

for a_tag in ul_tag.find_all('a'):

    # aタグのテキストを取得
    text = a_tag.text
    # aタグのhref属性を取得
    link_url = a_tag['href']
    # 表示します
    print(f'{text}: {link_url}')

'''

　　　　　↓↓↓処理結果↓↓↓
テスト1: http://example.com/1
テスト2: http://example.com/2
テスト3: http://example.com/3

'''


'''selectメソッド'''
'''
selectメソッドはfindメソッドと違ってリストで返してくる違いがある。
'''

'''
下記HTMLより商品名と価格を抽出する内容の場合。

<div class="item-list">
<div class="item" id="item-id-1">
<div class="item-left">
<img class="item-image" src='img/kaden_reizouko.png'>
</div>
<div class="item-right">
<a class="item-name" href="https://docs.pyq.jp/_static/assets/scraping/item-page1.html">
最新式冷蔵庫
</a>
<ul>
<li>価格: <span id="item-price">32,000円</span></li>
<li>発売日: <span class="item-release-date">2017-08-01</span></li>
<li>在庫: <span class="item-stock">10個</span></li>
</ul>
<p class="item-description">
最新式の冷蔵庫です。最新式の冷蔵庫です。最新式の冷蔵庫です。
最新式の冷蔵庫です。...
</p>
</div>
</div>
<-- 省略 -->
</div>

今回は対象のクラスは一つと仮定している
複数の場合は取得したリストをfor文などで利用。
'''

# 1.urlの変数を作る
url = '対象のURL'

# 2.対象のサイトからHTMLを取得
response = requests.get(url)
response.encoding = response.apparent_encoding

# 3.BeautifulSoupにHTMLを渡す。
bs = BeautifulSoup(response.text, 'html.parser')

# 4.cssセレクターを利用して要素の抽出
# 商品名の抽出
item_name_tags = bs.select('div.item-name')
item_name_tag = item_name_tags[0]
item_name = item_name_tag.text.strip()

# 価格の抽出
item_price_tags = bs.select('span #item-price')
item_price_tag = item_price_tags[0]
item_price = item_price_tag.text.strip()

# 5.表示
print(f'{item_name}:{item_price}')

'''

表示結果
最新式冷蔵庫：32,000円

'''


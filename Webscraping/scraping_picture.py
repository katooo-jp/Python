# 画像保存繰り返し作業自動化プログラム
# ログイン状態を維持してログイン後のページから画像を保存

from time import sleep
from bs4 import BeautifulSoup as bs
import requests, os


DOWNLOAD_PATH ="ダウンロードディレクトリのパス"
LOGIN_URL = "https://example.com/login"
PHOTO_PAGE_URL = 'https://example.com/photo'
# ログイン情報
LOGIN_MAIL = 'aaa@gexample.com'
LOGIN_PASS = 'password'


# セッション開始
session = requests.session()
ses = session.get(LOGIN_URL)

# 認証トークンの抽出
soup = bs(ses.text, 'html.parser')
auth_token = soup.find('input', {'name': '_token'}).get('value')
login_data = {
    '_token':auth_token,
	'email': LOGIN_MAIL,
	'password': LOGIN_PASS
}

# セッションにログイン情報を渡す
session.post(LOGIN_URL, data=login_data)

# 写真一覧ページから写真のリンクを抽出
sleep(1)
photo_soup = bs(session.get(PHOTO_PAGE_URL).text, "html.parser")
link_list = photo_soup.find_all('a', class_='img-card')
img_links = []
for link in link_list:
    img_links.append(link.get('href'))


# 画像の保存
for link in img_links:
    sleep(1)
    img = session.get(link).content
    img_name = link.split('/')[-1] # 画像の名前はURLの末尾がファイル名なのでそのまま利用
    img_path = os.path.join(DOWNLOAD_PATH, img_name)
    with open(img_path, 'wb') as f:
        f.write(img)
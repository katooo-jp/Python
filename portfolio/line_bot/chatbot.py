'''ただ悪口を返すだけのlinebotです。
需要はないと思いますが試しに作ってみました。'''

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import random

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#Webhookからのリクエストをチェック
@app.route("/callback", methods=['POST'])
def callback():
  # リクエストヘッダーから署名検証のための値を取得します。
  signature = request.headers['X-Line-Signature']

  # リクエストボディを取得します。
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  # handle webhook body
  # 署名を検証し、問題なければhandleに定義されている関数を呼び出す
  try:
    handler.handle(body, signature)
  # 署名検証で失敗した場合、例外を出す
  except InvalidSignatureError:
    abort(400)
  # handleの処理を終えればOK
  return 'OK'

######################################
'''LINEのメッセージの取得と返信内容の設定'''
######################################

#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合def以下の関数を実行
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークン。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡す

# 送信する内容をリスト化
send_list = ['黙れ','きもいって','口臭いしな','あーーーうるさ','はげ','デブ','ブス','バーカ','へー','あっそ','だから？',
'ただただきもいな','お前友達あんまおらんやろ？笑','生きてる価値なし','頭おかしいんじゃない？','あほ','インドにいけよ','うんこ野郎！',
'エロガッパが！！','偉そーにすんなよ','汚物が！','オタクが','カッコつけんなよ','消えろ','汚い！','キリストも殴るわ','刑務所帰れよ','消すぞ',
'けつでかい','チビ','腰抜け！','根性なし','ゴミ！！','最低だな','ささくれ野郎が！','三途の川いけよ','乳飲んどけ','しれっとすんなよ',
'しいたけ野郎が','少ない頭で考えろよ','スカスカな頭だな','精神おかしいよ','世界一きもい','性格悪すぎ','宝物壊すぞ？','ち◯こ野郎が','使えねえな',
'釣り合ってないよ','ヅラだろどうせ','敵ばっかだよお前','デブが！！！','木偶の坊が！','トイレの匂いする','とうもろこし野郎が','鈍臭いな',
'泣き虫が！','泣かせたろうか？','なめくじが！','人間離れした顔','ぬか漬けにしてやろうか？','脳みそ足りてる？','ノットニードユー','引きこもりが！',
'ヘタレが！','ボケ！','負け犬が！','まぬけ','ミートボールが！','ムカつく顔してるわお前','目が汚い','めんどくさいよ君','もういいよ。君',
'もうじき終わるよ君','ゆーことなし。帰れ','ラリってんな','冷静になれよ','歴史に残らないモブキャラが','わかったわかった','笑えないよ',
'おもしろくないよ','んーすごいね','んーダサいよ','んーと。特になし','粗チンが！','今まであった中で一番ち○こ小さいよ','小物だわー',
'好きだよ？','結婚しよ♡']

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  random_num = random.randint(0, len(send_list))
  send_message = send_list[random_num]

  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=send_message))


# ポート番号の設定
if __name__ == "__main__":
# app.run()
  port = int(os.getenv("PORT", 5000))
  app.run(host="0.0.0.0", port=port)


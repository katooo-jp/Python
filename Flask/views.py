'''Flask'''
'''
3大機能
・ルーティング
・テンプレートエンジン
・セッション
'''

from flask import Flask, render_template, request, url_for, redirect, session


'''Flaskのオブジェクトを生成。appはFlaskのオブジェクト名'''
app = Flask(__name__)


'''ルーティング'''
'''@app.route("/hello") と指定するとhttp://ドメイン名/hello というURLで
サイトにアクセスされた場合は hello_world 関数が実行
/helloの部分はurlのコンテキストパスという'''
@app.route('/hello')
def hello_world():
  return 'Hello, World!'


'''変数などの引き渡し'''
'''
render_template関数は、templatesフォルダを起点としたパスを引数に指定
第二引数以降で変数やリストなどをhtmlに渡せる。html側では　{{ 変数名 }}をタグに埋め込んでいる
'''
@app.route('/')
def index():
  greeting = 'こんにちは'
  return render_template('index.html', hello=greeting)




'''クエリストリング'''
'''
クエリストリングとは、Webサーバーに追加で情報を与えるためにURLに付け加える情報
コンテキストパスに続けて ? を書き、続けて key=value 形式でデータを書く
'''
fruits = {'1': 'もも', '2': 'みかん', '3': 'いちご'}
@app.route('/res/<no>/')
def result(no):
  # no = request.args.get('no', '1')
  return render_template('result.html',
                          fruit=fruits[no],
                          no=no)
'''
request.args.get は関数が呼び出されたときリクエストから値を取り出す。
（この場合は /res?no=1 の ? 以降が args）
?以降のno=1がargsに辞書のような形式で入っている

request.args["no"] とした場合、もし no が取得できなかった場合は KeyError。
request.args.get('no') とした場合はエラーにはならず、 None を取得できる。None がデフォルト値。
初期値を別の値にする場合第2引数に指定。今回は１を指定。
引数にnoを入れているのでコメントアウト。

result関数の引数はURLのnoを受け取るため
'''


'''formよりデータを受け取る'''
'''
GETはURLのクエリストリンク?key=xxxから情報を受け取る。
formを送信するとurlが/output?input=入力値となる
getする時の名前はformのnameで変えれる。今回はinput
'''
@app.route('/out/<no>/')
def output(no):
  name = request.args.get('input', '')
  return render_template('output.html',
                          name=name,
                          fruit=fruits[no])



'''validate'''
@app.route('/input')
def input():
  return render_template('input.html')

'''
ifでformから受け取った内容を確認して一致してない場合はerror文とともに再度input.htmlを返す

一致している場合はredirectで成功表示用のsuccess関数へ飛ばす。
'''
@app.route('/validate', methods=['POST'])
def validate():
  name = request.form['name']
  name2 = request.form['name2']

  if name != name2:
    error = '入力項目が一致していません'
    return render_template('input.html', error=error)
  
  return redirect(url_for('success'))

@app.route('/success')
def success():
  return render_template('success.html')


'''login:session'''
'''
画面から何もデータを送信していないのに、自分のユーザー名が毎回表示されるなど
複数の画面で状態を共有する仕組みがセッション（Session）という。
'''
# Flaskでは暗号化のための文字列secret_keyを決める必要がある。自由に決めれる。
app.secret_key = 'JiyuuNIkimereru'
@app.route('/login')
def login():
  user_name = request.args.get('name', '')
  if user_name:
    session['user_name'] = user_name
    return redirect(url_for('todo'))
  else:
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
  '''logout時はsessionをクリアする'''
  session.clear()
  return redirect(url_for('index'))

@app.route('/todo', methods=['GET', 'POST'])
def todo():
  if 'user_name' not in session:
    return redirect(url_for('index'))
  
  if request.method == 'POST':
    todo = request.form['todo']
    if todo:
      todo_list = []
      '''すでにsessionにtodoがあればsessionからtodoを取り出す'''
      if 'todo' in session:
        todo_list = session['todo']

      '''新しいtodoを追加してsessionに上書き'''
      todo_list.append(todo)
      session['todo'] = todo_list
  
  return render_template('todo.html')

@app.route('/todo_clear')
def todo_clear():
  '''session.popでsessionにある値を削除する'''
  session.pop('todo')
  return redirect(url_for('todo'))


'''おまじない'''
if __name__ == "__main__":
    app.run(debug=True)
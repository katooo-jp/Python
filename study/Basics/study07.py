'''Python OSモジュール'''

import os
from posix import times_result

'''ディレクトリ名とファイル名の引数でファイルの情報を確認できる関数'''
def search(target_path, file):
  '''joinでpathとして利用できる状態につなぐ'''
  path = os.path.join(target_path, file)
  
  '''os.path.exists(path)は指定したpathが存在するか確認できる'''
  if os.path.exists(path):
    print(path + 'は存在します。')
  else:
    print(path + 'は存在しません。')
  
  '''os.path.isfile(path)は指定したpathがファイルか判定'''
  if os.path.isfile(path):
    print(path + 'はファイルです。')
  
  '''os.path.isdir(path)は指定したpathがディレクトリーか判定'''
  if os.path.isdir(path):
    print(path + 'はディレクトリーです。')


'''os.listdir()はpathで指定されたディレクトリー内のファイル名と子ディレクトリー名が入ったリストを返す'''
def directory_list(target_path):
  for name in os.listdir(target_path):
    print(name)


def directory_tree(target_path):
  for root, dirs, files in os.walk(target_path):
    print(root) #ルートディレクトリ
    for drc in dirs: 
      print('\t', drc) #ディレクトリ名
    for file in files:
      print('\t', file) #ファイル名
  '''os.walk(top) は top をディレクトリーのツリーの基準（親）として、そのツリーに含まれる、 
  (top 自身を含む ) 各ディレクトリーごとに、タプル (root, dirs, files) を返す
  例）
  .
  └──test
      ├──a
      |  ├──a.py
      |  └──b.py
      ├──b
      |  └──c.py
      ├──d.py
      └──e.py
  の構成の場合
  test　
    a　
    b　
    d.py　
    e.py　
  a
    a.py
    b.py
  b
    c.py
と表示される

for root, dirs, files in os.walk(target_path):
  for name in files:
    path = os.path.join(root, name)
    print(path)
の場合は
test/a/a.py
test/a/b.py
test/b/c.py
test/d.py
test/e.py
のように表示される。

ルート内のディレクトリの中身は最後のfilesだけを割ればいい'''


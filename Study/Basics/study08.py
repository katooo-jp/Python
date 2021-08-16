'''matplotlib'''

import matplotlib.pyplot as plt
'''
matplotlib.pyplotにはグラフ描画などの多くの機能が用意されている。
！コードの記述方法は　"MATLABスタイル"　と　"オブジェクト指向スタイル"　の二種類
'''

'''折れ線グラフ'''
# MATLABスタイル
'''
！style.useでグラフのスタイル指定。plt.style.availableでスタイルの種類が確認できる。
！titleでグラフのタイトルの出力指示。
plotで折れ線グラフの出力指示。色は決められたものから順に使われる。
！plt.show()で表示。
'''
plt.style.use('seaborn-darkgrid')
plt.title('Test Graph')
plt.plot([2,1,3])
plt.plot([1,3,2])
plt.show()


# オブジェクト指向スタイル
'''
！最初の記述で描画オブジェクト（fig）とサブプロット（ax）を作成
・描画オブジェクトは、描画対象
・サブプロットは、1つの描画オブジェクトに複数作成できる配置場所

！plt.plotの代わりにax.plotで描画
最初の記述は1つのaxに対し2回plotを呼んでいるので、1枚のグラフに2本の折れ線グラフが描画される。

！plt.subplots(n, m)とすることで、n行m列のグリッド状のサブプロットを作成できる。
！ax[1].set_title('title')で各plotのタイトルを変更できる。

！fig.tight_layout()は、サブプロット間の位置関係を調整する関数.
これを実行しないと、タイトルが軸ラベルに重なって表示される。
'''
# 最初のグラフと同じ
fig, ax = plt.subplots()
ax.plot([2,1,3])
ax.plot([1,3,2])


# 縦並びver
fig, ax = plt.subplots(2) #2行
ax[0].plot([2,1,3])
ax[0].set_title('Subplot 1')
ax[1].plot([1,3,2])
ax[1].set_title('Subplot 2')
fig.tight_layout()

# 横並びver
fig, ax = plt.subplots(1,2) #１行２列
ax[0].plot([2,1,3])
ax[0].set_title('Subplot 1')
ax[1].plot([1,3,2])
ax[1].set_title('Subplot 2')
fig.tight_layout()

# 上記と同じグラフをMATLABスタイルで記述
plt.subplot(2, 1, 1)
plt.plot([2, 1, 3])
plt.title('Subplot 1')
plt.subplot(2, 1, 2)
plt.plot([1, 3, 2])
plt.title('Subplot 2')
plt.tight_layout()

'''
！凡例の描画方法
凡例は、legendで描画しますが、2通りの記述方法
・方法1：各グラフの描画時に凡例のラベルを指定する方法
・方法2：凡例の描画時に、まとめてラベルを指定する方法
修正しやすいため方法１がおすすめ。

！X軸ラベルはset_xlabelで変更。
！Y軸ラベルはset_ylabelで変更。

！項目名はset_xticks()とset_xticklabels()でX軸を変更。

！グラフの色や線の種類はcolorやlinestyleなどのオプションで変更できる。
'''

# 方法１
fig, ax = plt.subplots()
ax.plot([2, 1, 3], label='sample 1')
ax.plot([1, 3, 2], label='sample 2')
ax.legend()

# 方法２
fig, ax = plt.subplots()
ax.plot([2, 1, 3])
ax.plot([1, 3, 2])
ax.legend(['sample 1', 'sample 2'])

# ラベルの変更
fig, ax = plt.subplots()
ax.plot([2,1,3])
ax.set_xlabel('X label')
ax.set_ylabel('Y label')

# 項目名の変更
fig, ax = plt.subplots()
x = [1,2,3]
ax.plot(x, [2,1,3])
ax.set_xticks(x)
ax.set_xticklabels(['Item1', 'Item2', 'Item3'])

# グラフの色などの変更
fig, ax = plt.subplots()
ax.plot([2,1,3], color='r', marker='s', linestyle='--', linewidth=3)

# グラフの色などの変更（省略形）
fig, ax = plt.subplots()
ax.plot([2,1,3], 'rs--', linewidth=3)


'''棒グラフ'''
'''
積み上げ棒グラフにするには、棒の下辺（bottom）を前のデータの累積和にする
・赤いグラフ（一段目）：最初のデータなので、bottomは指定しない。
・青いグラフ（二段目）：bottomに、赤いグラフのデータであるy1を指定。
もし、3つ目のグラフがあれば、bottomに、y1とy2を要素ごとに足したリストを指定
'''

# データ
w = 0.4  # width
x1 = [0, 1, 2]
x2 = [w, 1 + w, 2 + w]
y1 = [1, 2, 3]
y2 = [3, 1, 2]

# 横に並んだ棒グラフ
fig, ax = plt.subplots()
ax.bar(x1, y1, width=w, color='r', alpha=0.5)
ax.bar(x2, y2, width=w, color='b', alpha=0.5);

# 積み上げ棒グラフ
fig, ax = plt.subplots()
ax.bar(x1, y1, width=w, color='r', alpha=0.5)
ax.bar(x1, y2, bottom=y1, width=w, color='b', alpha=0.5);

'''円グラフ'''
'''
！円グラフはpie(x,...)のxでグラフの割合のリストを設定
explode=[0, 0.1, 0]と指定することで、2番目の扇形を中心から半径×0.1だけ離す。
autopctで少数第１までを％で表示を指定。
startangle=90, counterclock=Falseとすることで、上から時計回りに項目を表示。
startangleは（時計の3時が0度で、反時計回り）
counterclockは表示を反時計回りか。Falseで時計回りになる。

ax.axis('equal')の'equal'は、「縦と横の比率（アスペクト比）を1にする」。
これで円グラフの円が真円になる。
'''
fig, ax = plt.subplots()
ax.pie([2,1,3], explode=[0,0.1,0],
      labels=['Item 1', 'Item 2', 'Item 3'],
      autopct='%.1f%%',startangle=90, counterclock=False);
ax.axis('equal')
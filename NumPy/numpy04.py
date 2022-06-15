'''
===NumPy Basics(4)===


===ユニバーサル関数===
以下のような関数をユニバーサル関数という
・引数は、多次元配列（またはリストなど）
・引数の各要素ごとに演算
・結果は、引数と同じサイズの多次元配列（ndarray）
'''

# 例題）2000個の薄い小物があります。この小物を貸倉庫に預けようと考えました。
# 貸倉庫では、小物がぎりぎり入る長方形の対角線の長さに比例して費用がかかるそうです。
'''
===対角線の長さの計算===
対角線の長さは　√高さ**2 + 幅**2　で求める
平方根の計算はmath.sqrt(幅**2 + 高さ**2)で計算できるが配列に対応していない

numpy.sqrtなら多次元配列のまま計算可能
'''

import numpy as np
import math

width = np.random.randint(50, 100, 2000)
height = np.random.randint(50, 100, 2000)

square = width**2 + height**2
anser = np.sqrt(square)


'''
===ユニバーサル関数の作成===
numpy.vectorizeで、ユニバーサル関数でない関数をユニバーサル関数にできる
'''

try:
  square = math.sqrt(width**2 + height**2)
except TypeError as e:
  print(e)
# only size-1 arrays can be converted to Python scalars

a = np.vectorize(math.sqrt)
anser2 = a(width**2 + height**2)

b = anser == anser2
b[:3] # [ True  True  True]


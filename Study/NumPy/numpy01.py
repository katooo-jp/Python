'''
===NumPy Basics===
NumPyは多次元配列を効率よく扱える
多次元配列とは、0次元配列、1次元配列、2次元配列などのn次元配列のこと

・1次元配列はベクトル
・2次元配列は行列
・3次元以上の配列はテンソルと呼ぶ。
・次元のない（0次元の）値は、スカラーと呼ぶ。
numpy.arrayで、0次元配列も作成できるが、intやfloatを使えば良いので使われない。
'''

import numpy as np
from numpy.core.function_base import linspace
from numpy.core.numeric import full, full_like, ones_like
from numpy.lib.twodim_base import diag, eye

# 一次元配列
a = np.array([1,2,3])

# 二次元配列
b = np.array([[1,2,3],[4,5,6]])
b[0][2] # 3
b[1][0] # 4
b[0,2] # 3

# 三次元配列
c = np.array([ [[1,2,3],[4,5,6]], [[11,12,13],[14,15,16]] ])
c[1,0,2] # 13
c[0,1,1] # 5

type(a)
type(b)
type(c)
# 全てnumpy.ndarray

'''
===numpy.ndarrayの主なプロパティー===
・ndim	次元数
・shape	各次元のサイズのタプル
・size	要素数
・reshape　次元数や各次元のサイズ変更
'''

# ndim 次元数
a.ndim # 1
c.ndim # 3

# shape	各次元のサイズのタプル
b.shape # (2,3)
c.shape # (2,2,3)

# size	要素数
a.size # 3
c.size # 12

# reshape　次元数や各次元のサイズ変更
b.reshape(6) # [1,2,3,4,5,6]
b.reshape(2,3) # [[1,2,3], [4,5,6]]

'''
===同じ要素で配列を作る===
・zeros(サイズ): 全ての要素が0の多次元配列
・ones(サイズ): 全ての要素が1の多次元配列
・full(サイズ, 値): 全ての要素が値の多次元配列
'''

# zeros
a = np.zeros(3) # [0., 0., 0.]

# ones
b = np.ones(3) # [1., 1., 1.]
c = np.ones((2,3)) # [[1., 1., 1.], [1., 1., 1.]]

# full
d = np.full((2,3), 5) # [[5.,5.,5.],[5.,5.,5.]]

'''
===shapeが同じ多次元配列からの作成===
・zeros_like(多次元配列): 要素が全て0の多次元配列
・ones_like(多次元配列): 要素が全て1の多次元配列
・full_like(多次元配列, 値): 要素が全て値の多次元配列
'''

# zeros_like
d = np.zeros_like(d) # [[0.,0.,0.], [0.,0.,0.]]

# ones_like
d = np.ones_like(d) # [[1.,1.,1.], [1.,1.,1.]]

# full_like
d = np.full_like(d, 3) # [[3.,3.,3.], [3.,3.,3.]]

# int型指定
d = np.full_like(d, 7, dtype=int) # [[7,7,7], [7,7,7]]

'''
===主な生成関数===
・arange(start, end, step, dtype=None) range関数と同じ使い方だが型の指定ができる
・linspace(start, end, 個数, dtype=None) 始まりと終わりを指定して個数分要素の作成
・eye(サイズ)　対角線が全て1の単位行列
・diag(指定する配列)　任意の対角行列
'''

# arange
a = np.arange(5) # [0,1,2,3,4]
b = np.arange(2, 5, dtype=float) # [2.,3.,4.] 
c = np.arange(3,9,3) # [3,6,9]

# linspace
d = np.linspace(1, 3, 5) # [1, 1.5, 2, 2.5, 3]

# eye
e = np.eye(3) # [[1,0,0], [0,1,0], [0,0,1]]
f = np.eye(3, 4) # [[1,0,0,0], [0,1,0,0], [0,0,1,0]]

# diag
g = np.diag([1,2,3]) # [[1,0,0],[0,2,0],[0,0,3]]


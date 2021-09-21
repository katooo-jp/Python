'''
===NumPy Basics(2)===


===ブロードキャスト===
NumPyでは基本的に、同じインデックスの要素ごとに演算する。
同じ次元数、かつ、各次元のサイズも同じであれば問題ないが
異なる場合は、次元数の小さい方を複製してデータを揃えようとする。
これをブロードキャストと呼ぶ。
'''
import numpy as np

a = np.arange(8).reshape(2,2,-1)
'''
[[[0, 1],[2, 3]],
[[4, 5],[6, 7]]]
'''

a + a
'''
[[[0, 2],[4, 6]],
[[8, 10],[12, 14]]]
'''

b = np.array([[10,11],[12,13]])

a + b
'''
[[[10, 12],[14, 16]],
[[14, 16],[18, 20]]]
'''

c = np.array([b, b])
'''
[[[10, 11],[12, 13]],
[[10, 11],[12, 13]]]
'''

a + c
'''
[[[10, 12],[14, 16]],
[[14, 16],[18, 20]]]
'''


'''
===ブロードキャストできるものとできないもの判断方法===
ブロードキャストは、「形状の次元数を揃えたときに、全次元のサイズが『同じか、片方が1』となる」ときにできる。
これは、形状（shape）を見ることで判断できる。また、次元数は形状の個数

！！形状の次元数を揃える方法は、「次元数が同じになるまで、形状に、左から1を足す」！！
例)　サイズ(3,2,4)のndarrayに対して和を求めようとした時
・ブロードキャストできないもの
np.zeros(2)：　(2)　→　(1, 1, 2)
np.zeros(3)：　(3)　→　(1, 1, 3)
np.zeros((1, 2))：　(1, 2)　→　(1, 1, 2)
np.zeros((1, 3))：　(1, 3)　→　(1, 1, 3)
np.zeros((2, 2))：　(2, 2)　→　(1, 2, 2)
np.zeros((2, 3))：　(2, 3)　→　(1, 2, 3)
np.zeros((3, 1))：　(3, 1)　→　(1, 3, 1)
np.zeros((3, 2))：　(3, 2)　→　(1, 3, 2)
np.zeros((1, 1, 2))：　(1, 1, 2)　→　(1, 1, 2)
np.zeros((2, 1, 4))：　(2, 1, 4)　→　(2, 1, 4)

！！上記例の判断方法　(3,2,4)と比較して『同じか、片方が1』でOK！！
(1, 1, 2)　と　(3, 2, 4)：　1と3はOK。1と2はOK。2と4はNG。
(1, 1, 3)　と　(3, 2, 4)：　1と3はOK。1と2はOK。3と4はNG。
(1, 2, 2)　と　(3, 2, 4)：　1と3はOK。2と2はOK。2と4はNG。
(1, 2, 3)　と　(3, 2, 4)：　1と3はOK。2と2はOK。3と4はNG。
(1, 3, 1)　と　(3, 2, 4)：　1と3はOK。3と2はNG。1と4はOK。
(1, 3, 2)　と　(3, 2, 4)：　1と3はOK。3と2はNG。2と4はNG。
(2, 1, 4)　と　(3, 2, 4)：　2と3はNG。1と2はOK。4と4はOK。
どれも次元のどこかでNGがあるのでブロードキャストできない。
'''


'''
===ブロードキャストして代入===
'''
a = np.arange(4)
b = np.arange(8).reshape(2,4)
c = np.arange(12).reshape(3,1,4)

data = np.zeros((3,2,4))
'''
[[[0,0,0,0],
[0,0,0,0]],

[[0,0,0,0],
[0,0,0,0]],

[[0,0,0,0],
[0,0,0,0]]]
'''

data[:] = a
'''
[[[0,1,2,3],
[0,1,2,3]],

[[0,1,2,3],
[0,1,2,3]],

[[0,1,2,3],
[0,1,2,3]]]
'''

# +=　の代入には[:]はいらない。
data += b
'''
[[[0,1,2,3],
[4,5,6,7]],

[[0,1,2,3],
[4,5,6,7]],

[[0,1,2,3],
[4,5,6,7]]]
'''

data = c
'''
[[[0,1,2,3],
[0,1,2,3]],

[[4,5,6,7],
[4,5,6,7]],

[[8,9,10,11],
[8,9,10,11]]]
'''


'''
===ブールインデックス参照で代入===
比較の式でブールインデックス参照を使い条件に合致した部分に簡単かつ高速に代入できる。
'''

a = np.arange(12).reshape(3, -1)
'''
[[0,1,2,3],
[4,5,6,7],
[8,9,10,11]]
'''

# 偶数に0を代入する
b = a.copy()
b[b % 2 == 0] = 0
'''
[[0,1,0,3],
[0,5,0,7],
[0,9,0,11]]
'''

# AND は &（アンパサンド）を使う
c = a.copy()
c[(4 <= c) & (c < 8)] = 0
'''
[[0,1,2,3],
[0,0,0,0],
[8,9,10,11]]
'''

# OR は |（パイプ）を使う
d = a.copy()
d[(d == 1) | (d == 5)] = 0
'''
[[0,0,2,3],
[4,0,6,7],
[8,9,10,11]]
'''


# NOT は ~（チルダ）を使う
e = a.copy()
e[~(e == 7)] = 0
'''
[[0,0,0,0],
[0,0,0,7],
[0,0,0,0]]
'''
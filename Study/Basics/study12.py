'''
＝＝＝二分探索＝＝＝

＝serach関数の目的＝
同じ長さの棒をN本作るときそれぞれ違う長さの棒がlstにある。
lstに入っている長さを使って同じ長さの棒を作るときに
何cmであればN本作れるかを求める。s

＝search関数の手順＝
・杖の長さの下限と上限を決める。
  下限loは0にする。
    loの長さであればN本以上作成できる。
  上限upは、全ての棒の長さの和をNで割ったものとする。
    upの長さだと、N本作成できない。
・up - loが1を超えている間、以下を繰り返す。
  中間点midを(lo + up) // 2とする。
  杖の長さをmidとしたときの本数をnumに入れる。
    棒の長さがlのとき、杖はl // mid本できる。
  num >= Nのとき、midでN本以上作成できるので、lo = midとする。
  num < Nのとき、midでN本作成できないので、up = midとする。
・loの長さであればN本以上作成できるので、loを返す。

search(lst)で計算すると、杖の長さは、29になる。
[l // sl for l in lst]で各棒からできる杖の本数がわかる。
合計するとN本になることが確認できる。

＝まとめ＝
答え（杖の長さ）があれば、その答えが条件を満たしている（30本以上ある）か、
簡単にわかる問題の場合、答えを二分探索することで、効率良く計算できます。
'''

N = 30
lst = [59, 126, 215, 236, 265]  # 各棒の長さ

def search(lst):
  lo = 0  # 杖の長さの下限
  up = sum(lst) // N  # 杖の長さの上限
  while up - lo > 1:
    mid = (lo + up) // 2  # 中間点
    print(f'途中経過 {lo} - {mid} - {up}')
    num = sum(l // mid for l in lst)  # 本数
    if num >= N: # 本数十分
      lo = mid
    else:  # 本数不足
      up = mid
  return lo

sl = search(lst)
print('杖の長さ', sl)

'''
=表示=
途中経過0 - 15 - 30
途中経過15 - 22 - 30
途中経過22 - 26 - 30
途中経過26 - 28 - 30
途中経過28 - 29 - 30
杖の長さ 29
'''

nums = [l // sl for l in lst]
print(nums) # 各棒からできる杖の本数
'''
=表示=
[2, 4, 7, 8, 9]
'''

sum(nums) == N  #  全部でN本
'''
=表示=
True
'''
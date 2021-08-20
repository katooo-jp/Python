'''アルゴリズム'''

'''
ーーーエラトステネスのふるいーーー
素数を列挙するアルゴリズムの一つ
'''

def primes(max_num):
  result = [2]
  if max_num == 2:
    return result

  pr = list(range(3, max_num, 2))
  npr = len(pr)

  for i, n in enumerate(pr):
    if n:
      if n * n > max_num: 
        break
      # 合成数を0に変えるループ
      for j in range(i + n, npr, n):
        pr[j] = 0
  
  for i in pr:
    if i: #0の時は追加しない。
      result.append(i)
  return result

print(primes(20))

'''
表示
[2, 3, 5, 7, 11, 13, 17, 19]


解説
指定した数までの素数を列挙する関数。
最初に「指定された数までの整数」を用意。数の小さい方から見ていき、素数として見つかった数の合成数を消していく。

・偶数の素数は2だけ。2を特別扱いとして、探索対象を3以上の奇数とする
・n * n > 指定された数であれば、n以上は探索不要

流れ
1.最初に2の入ったリストresultを作り、引数が２であればそのリストを返して処理終了
2.3からnまでの奇数のリストprを作成
3.prの各要素（n）について、下記を繰り返す（繰り返し回数はi）
  ・if n:で０の処理を飛ばす。
  ・nが0ではない、つまり素数の場合、下記を実行
    ・n * n > max_numならば、ループを抜ける
    ・pr[i]は、素数。pr[i]の倍数は合成数なので、0に置き換え。pr[i + n]からn個飛びに0を代入。
4.あとはresultにprの内容を追加していく。

！！！point！！！
・n * n > max_numに該当しない場合は探索が不要である
・合成数を０に変えるループfor j in range(i + n, npr, n)は
3 * n == pr[i + 1 * n]
5 * n == pr[i + 2 * n]
7 * n == pr[i + 3 * n]
9 * n == pr[i + 4 * n]
なのでprからそれぞれの素数の合成数のみ０に変えていける。
'''
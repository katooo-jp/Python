# RPGのバトルの一場面作成
# 勇者とスライムの一騎打ち
# timeモジュールで時間を置いて表示

import random
import time

# 勇者のHPは30固定　スライムは1〜30でランダム
yusha_hp = 30
monster_hp = random.randint(1, 30)

print('スライムがあらわれた！')
print('スライムHP =', monster_hp)
time.sleep(1)

while True:
    print('ゆうしゃのこうげき！')
    time.sleep(1)
    num = random.randint(0,10)
    print(f'スライムに{ num }のダメージ')
    monster_hp -= num
    time.sleep(1)

    if monster_hp <= 0:
        print('スライムをやっつけた')
        break

    print('スライムのこうげき！')
    num = random.randint(0,10)
    time.sleep(1)
    print(f'ゆうしゃに{ num }のダメージ')
    yusha_hp -= num
    time.sleep(1)

    if yusha_hp <= 0:
        print('ゆうしゃはしんでしまった')
        break
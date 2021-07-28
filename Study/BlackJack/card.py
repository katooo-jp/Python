'''BlackJack'''
# ジョーカー抜きの52枚の山札生成クラス

class Card:
    def __init__(self, num):
        self.suit = num // 13 + 1
        self.rank = num % 13 + 1

    def point(self):    
        return min(10, self.rank)
    
    def __str__(self):
        s = '♦♥♠♣'[self.suit - 1]
        r = 'Ａ⒉⒊⒋⒌⒍⒎⒏⒐⒑ＪＱＫ'[self.rank - 1]
        return s + r


if __name__ == '__main__':
    '''0〜51までの引数でカードの柄と数字を返す。'''
    print(Card(0))  # ♦Ａ
    print(Card(1))  # ♦⒉
    print(Card(13))  # ♥Ａ

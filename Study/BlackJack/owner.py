'''BlackJack'''
# 山札(cards)より1枚ドローと現在の手札とポイント表示クラス


class Owner:
    def __init__(self):
        self.hands = []
        
    # 山札より1枚手札に移動
    def draw(self, bj):
        self.hands.append(bj.pop())

    # 現状の手札表示
    def sequence(self, hide=False):
        s = ''.join(str(cd) for cd in self.hands)
        return s[:2] + '＊＊' + s[4:] if hide else s

    # 手札のポイント表示
    def point(self):
        p = sum(cd.point() for cd in self.hands)
        for cd in self.hands:
            if cd.rank == 1 and p + 10 <= 21:
                p += 10
        return p


if __name__ == '__main__':
    from main import Blackjack
    
    bj = Blackjack(7)
    own = Owner()
    own.draw(bj)
    own.draw(bj)
    print(own.sequence(), own.point())  # ♥⒌♣Ａ 16
    own.draw(bj)
    print(own.sequence(), own.point())  # ♥⒌♣Ａ♠⒍ 12

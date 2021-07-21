'''BlackJack'''
# ディーラーの行動管理クラス
# ディーラーはポイントが１６以下であればドローを続ける仕様

from owner import Owner

class Dealer(Owner):
    def act(self, bj):
        while self.point() <= 16:
            self.draw(bj)


if __name__ == '__main__':
    from main import  Blackjack

    bj = Blackjack(11)
    dealer = Dealer()
    dealer.act(bj)
    print(dealer.sequence())  # ♥⒍♦⒌♥⒌♥⒊
    bj = Blackjack(2)
    dealer = Dealer()
    dealer.act(bj)
    print(dealer.sequence())  # ♥⒊♠⒋♦⒑

'''BlackJack'''
# ゲームの管理クラス


import random
from card import Card
from player import Player
from dealer import Dealer


class Blackjack:
    def __init__(self, seed):
        self.cards = [Card(i) for i in range(52)]
        random.seed(seed)
        random.shuffle(self.cards)
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        # プレイヤーとディーラーに2枚づつ交互に配る
        for _ in range(0,2):
            self.player.draw(self)
            self.dealer.draw(self)
        # プレイヤーの行動ポイント表示
        self.player.act(self)
        player_point = self.player.point()
        # プレイヤーのポイントが２１を超えていなければディーラーのフェイズに移り勝敗表示。
        self.message = 'You lose.'
        if player_point <= 21:
            self.dealer.act(self)
            dealer_point = self.dealer.point()
            if player_point == dealer_point:
                self.message = 'Draw.'
            elif dealer_point >= 22 or dealer_point < player_point:
                self.message = 'You win.'
        self.show(False)
        print(self.message)

    def show(self, hide):
        p = self.player.point()
        s = self.player.sequence()
        print(f'Player({p}): {s}')
        d = self.dealer.point()
        k = self.dealer.sequence(hide)
        print(f'Dealer({d}): {k}')

    def pop(self):
        return self.cards.pop(0)


if __name__ == '__main__':
    num = random.randint(0, 10000)
    bj = Blackjack(num)  # 引数が変わると山札も変わる
    bj.start_game()

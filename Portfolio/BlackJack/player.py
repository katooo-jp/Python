'''BlackJack'''
# プライヤーの行動管理クラス
# プレイヤーはn以外の入力でドローを続けることができる。

from owner import Owner

class Player(Owner):
    def ask(self):
        print('もう1枚引く？（y/n）', end='')
        return input()

    def act(self, bj):
        while self.point() <= 20:
            bj.show(True)
            s = ''
            if s != 'y' and s != 'n':
                s = self.ask()
            if s == 'n':
                break
            self.draw(bj)
                
                


if __name__ == '__main__':
    from main import Blackjack

    bj = Blackjack(0)
    player = Player()
    commands = list('yyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♠⒊♦Ｋ
    bj = Blackjack(3)
    player = Player()
    commands = list('yyyyyyyyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♥Ａ♠⒊♦⒋♥⒎♠⒋♠Ａ♣Ｋ
    bj = Blackjack(4)
    player = Player()
    commands = list('yyyyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♠Ｑ♥⒑♣Ａ

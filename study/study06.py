# 自動販売機のシステム作成

import random

class Drink:
    def __init__(self, name, price, stock):
        self.name = name  # 名称
        self.price = price  # 価格
        self.stock = stock  # 在庫

    def info(self):
        """情報（名称と価格）を返す"""
        return f'{self.name} {self.price}円'


class VendingMachine:
    def __init__(self):
        self.drink_list = []  # 飲み物一覧

    def show_all(self):
        """全ての飲み物を表示"""
        for drink in self.drink_list:
            print(drink.info())

    def add_drink(self, drink):
        """1種類の飲み物を登録"""
        self.drink_list.append(drink)

    def select_drink(self, kth):
        """kth番目の飲み物の情報を返す"""
        return self.drink_list[kth].info()
    
    def show_selected_drink(self, kth):
        drink = self.drink_list[kth]
        if drink.stock > 0:
            print(f'{drink.name}を選択しました。{drink.price}円になります')
        else:
            print(f'{drink.name}は売り切れています。申し訳ありません')
            
    def gacha(self):
        return random.randint(1,5) == 1
    
    def purchase_drink(self, kth, fee):
        drink = self.drink_list[kth]
        print(f'{fee}円が投入されました')
        if fee < drink.price:
            print('購入金額が足りません')
            return
        change = fee - drink.price
        if change > 0:
            print(f'{change}円のお釣りになります')
        drink.stock -= 1
        if drink.stock > 0 and self.gacha():
            print('大当たりーーー')
            print(f'もう1本 「{drink.name}」を差し上げます！')
            drink.stock -= 1
    
vm = VendingMachine()
vm.add_drink(Drink('珈琲', 130, 10))
vm.add_drink(Drink('お茶', 150, 12))
vm.add_drink(Drink('サイダー', 110, 2))

print('=== 全商品の表示 ===')
vm.show_all()

print('\n=== 3番目の商品のボタンを押します ===')
vm.show_selected_drink(2)

print('\n=== 3番目の商品を選択し100円を投入 ===')
vm.purchase_drink(2, 100)

print('\n=== 3番目の商品を選択し150円を投入 ===')
vm.purchase_drink(2, 150)

print('\n=== 3番目の商品のボタンを押します ===')
vm.show_selected_drink(2)

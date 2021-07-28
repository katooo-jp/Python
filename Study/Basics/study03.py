# 西暦を和暦に変更する関数作成


# 西暦から和暦へ変換する関数
def convert_japanese_year(ad):
    if ad < 1926:
        wareki = '昭和以前'
    elif ad < 1989:
        wareki = f'昭和{ad - 1926 + 1}年'
    elif ad < 2019:
        wareki = f'平成{ad - 1989 + 1}年'
    else:
        wareki = f'令和{ad - 2019 + 1}年'
    return wareki

# 表示関数
def main():
    wareki_2020 = convert_japanese_year(2020)
    print('西暦2020年は', wareki_2020)

    wareki_2000 = convert_japanese_year(2000)
    print('西暦2000年は', wareki_2000)

    wareki_1975 = convert_japanese_year(1975)
    print('西暦1975年は', wareki_1975)


if __name__ == '__main__':
    main()

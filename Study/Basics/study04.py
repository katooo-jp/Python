# 日付付きの西暦から和暦変換

from datetime import datetime

WAREKI_START = {'令和': datetime(2019, 5, 1),
                '平成': datetime(1989, 1, 8),
                '昭和': datetime(1926, 12, 25)}


def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    if datetime(y, m, d) >= WAREKI_START['令和']:
        anser_year = y - WAREKI_START['令和'].year + 1
        if anser_year == 1:
            anser_year = '元'
        anser = f'令和{anser_year}年'
    elif datetime(y, m, d) >= WAREKI_START['平成']:
        anser_year = y - WAREKI_START['平成'].year + 1
        if anser_year == 1:
            anser_year = '元'
        anser = f'平成{anser_year}年'
    elif datetime(y, m, d) >= WAREKI_START['昭和']:
        anser_year = y - WAREKI_START['昭和'].year + 1
        if anser_year == 1:
            anser_year = '元'
        anser = f'昭和{anser_year}年'
    else:
        anser = '昭和以前'
        
    return anser


def main():
    print('西暦2020年4月1日は、', convert_to_wareki(2020, 4, 1), sep='')
    print('西暦2019年5月1日は、', convert_to_wareki(2019, 5, 1), sep='')
    print('西暦2019年4月30日は、', convert_to_wareki(2019, 4, 30), sep='')
    print('西暦1989年1月8日は、', convert_to_wareki(1989, 1, 8), sep='')
    print('西暦1989年1月7日は、', convert_to_wareki(1989, 1, 7), sep='')
    print('西暦1974年5月5日は、', convert_to_wareki(1974, 5, 5), sep='')
    print('西暦1926年12月25日は、', convert_to_wareki(1926, 12, 25), sep='')
    print('西暦1926年12月24日は、', convert_to_wareki(1926, 12, 24), sep='')


if __name__ == '__main__':
    main()

# 模範解答
def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    # 入力された年月日をdatetime型に変換する
    input_date = datetime(y, m, d)

    for gengo, start_date in WAREKI_START.items():
        if input_date >= start_date:
            int_wanen = y - start_date.year + 1
            if int_wanen == 1:
                wanen = '元'
            else:
                wanen = str(int_wanen)
            return f'{gengo}{wanen}年'
    return '昭和以前'
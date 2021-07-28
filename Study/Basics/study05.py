# 読み込んだファイルのデータ集計
# report.txtのデータはカンマ区切りで書かれている
# 例
# 2015-06-01 09:00:00,コーラ,160
# 2015-06-01 13:16:00,ミネラルウォーター,110
# 2015-06-01 16:16:00,オレンジジュース,100
# 2015-06-01 20:27:00,コーラ,160

from datetime import datetime

# file読み込み関数
def sales_data():
    """売上データを取得."""
    result = []
    with open('input/report.txt', encoding='utf-8') as f:
        for row in f:
            columns = row.rstrip().split(',')
            sale_date = datetime.strptime(columns[0], '%Y-%m-%d %H:%M:%S')
            name = columns[1]
            price = int(columns[2])
            new_data = {'sale_date': sale_date,
                        'name': name,
                        'price': price}
            result.append(new_data)

    return result

# 集計関数
def total_sales_data(year, month):
    """売上データの集計."""
    s_data = sales_data()
    count = 0
    total = 0
    for i in range(0, len(s_data)):
      if s_data[i]['sale_date'].year == year and s_data[i]['sale_date'].month == month:
        total += s_data[i]['price']
        count += 1
    
    return count, total

# 表示関数
def main():
    """メインの処理."""
    r_count, r_total = total_sales_data(2015, 7)
    print(f'売上金額: {r_total:,}円')
    print(f'販売個数: {r_count}個')
    print(f'顧客単価: {r_total / r_count:,.2f}円')


if __name__ == '__main__':
    main()

# 最大公約数を求める関数gcdの作成
# ユークリッドの互除法
def gcd(a, b):
    if a > b:
        a, b = b, a
    
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b
                
print(gcd(638, 572))
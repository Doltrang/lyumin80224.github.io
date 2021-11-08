#最大公因數
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)
##########################
r= gcd(540,840)
if r == 1:
    print('互質')
else:
    print('最大公因數 ：',r)
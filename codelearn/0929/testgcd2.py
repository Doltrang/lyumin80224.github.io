#最大公因數
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n) #gcd(69,23) -> gcd(23,0) -> 23
##########################
r= gcd(69,23)
if r == 1:
    print('互質')
else:
    print('最大公因數 ：',r)
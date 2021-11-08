print(3&7)
print(3|7)
print(6&9)
print(6|9)

print(bin(3)) #0b11   0011
print(bin(7)) #0b111  0111       0b=二進位 0O=八進位 0X十六進位
print(bin(6)) #0b110  0110
print(bin(9)) #0b1001 1001

print(3^7) #0011^0111=0100
print(6^9) #0110^1001=1111

print(bin(8))   # 8      1000
print(~8)       # ~8=-9  0111
print(bin(~8))  #   0~ 127    01111111
                #  -1~-128    10000000


# 8 1000  >>2      2 10
print(8>>2)
print(2<<2)
#12 1100  >>2      3 11
#15 1111  >>2      3 11
print(12>>2)
print(3<<2)
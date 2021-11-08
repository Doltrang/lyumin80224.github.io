from sys import argv
try:
    num = 100/float(argv[1])
    print('1.程式正常執行')
except IndexError as ie:
    print('2.發生例外')
except ValueError as ve:
    print('3.發生例外')
finally:
    print('4.一定會發生')
print('5.程式受控制')
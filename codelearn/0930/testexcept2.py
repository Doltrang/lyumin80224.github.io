from sys import argv
try:
    num = int(argv[1])
    print(100/num)
except IndexError as ie:
    print('請輸入參數...')
except ValueError as ve:
    print('請輸入數字...')
except ZeroDivisionError as zde:
    print('請輸入非零的參數...')

#python TestExcept2.py 5
#20.0

#python TestExcept2.py
#IndexError

#python TestExcept2.py abc
#ValueError

#python TestExcept2.py 0
#ZeroDivisionError
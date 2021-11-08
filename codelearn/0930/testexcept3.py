from sys import argv
try:
    num = int(argv[1])
    print(100/num)
except IndexError:
    print('請輸入參數...')
except (ValueError,IndexError):
    print('請輸入數字...')
except:
    print('請輸入非零的參數...')

#python TestExcept2.py 5
#20.0

#python TestExcept2.py
#IndexError

#python TestExcept2.py abc
#ValueError

#python TestExcept2.py 0
#ZeroDivisionError
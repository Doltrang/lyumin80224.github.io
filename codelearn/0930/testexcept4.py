from sys import argv
try:
    num = int(argv[1])
    print(100/num)
except ZeroDivisionError as zde: #若zeroDivisionError在下方不會執行，因在ArithmeticError支項
    print('請輸入非零的參數...')
except ArithmeticError as ae:
    print('發生數值運算錯誤...')    
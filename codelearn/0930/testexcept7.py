from sys import argv
if len(argv) > 1:
    print(argv[1])
else:
    print('未輸入參數')

try:
    print('Hello')
finally:
    print('一定會執行')
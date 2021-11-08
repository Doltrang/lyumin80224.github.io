#千萬不要這樣寫
from sys import argv
try:
    num = int(argv[1])
    print(100/num)
except :
    pass
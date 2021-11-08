def a():
    text= None
    return text.upper()
def b():
    a()
def c():
    b()
#################
try:
    c()
except:
    print('發生例外')
    import traceback
    traceback.print_exc()

def some(*x,**y):
    print('x =',x)
    print('y =',y)
#####################
some()
some(10,20,30)
some(10,20,30,a=100,b=200,c=300)
some(a=100,b=200,c=300)
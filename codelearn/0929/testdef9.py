def test(x):
    x=20
    print(locals())
######################
x=10
test(x)
print(x)
print(locals())
print('----------------------------------')
def test2():
    global x
    x=20
    print(locals())
######################
x=10
test2()
print(x)
print(locals())
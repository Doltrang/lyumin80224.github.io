class A:
    def test1():
        print('test1')
    def test2(self):
        print('test2')
#############################
a=A()
a.test2()
# a.test1() #物件.方法
A.test1() #物件去呼叫function,自帶self過去
print(dir('Hello'))
print('Hello'.upper())
print(dir(10))
print((10).__add__(5))
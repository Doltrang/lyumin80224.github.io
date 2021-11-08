class A: #A(object)
    def __init__(self,msg):
        pass#未設計時會自動加入 def ___init__(self):
class B(A):
    def __init__(self):
        super().__init__()
        pass #上兩行為 未設計時會自動加入


######################
a = A('hello')
b = B()
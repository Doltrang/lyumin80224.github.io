class C:
    def __init__(self):
        print('C建構子被呼叫...')
class D(C):
    def __init__(self):
        print('D建構子被呼叫...')
        # super().__init__()

d= D()
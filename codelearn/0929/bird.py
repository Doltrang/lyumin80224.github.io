class Bird:
    def __init__(self,name):
        self.name=name
    def walk(self):
        return self.name+'會走路...'
    def __str__(self):
        return '我是一隻不會飛的小鳥'
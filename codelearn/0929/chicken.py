from bird import Bird

class Chicken(Bird):
    def walk(self):
        # return self.name+'會走路!!!'
        return super().walk()+'!!!'
        #super() 父類別的
    def wu(self):
        return self.name+'咕咕叫...'
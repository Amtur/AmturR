class Animal(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
a1=Animal('cat')
print a1

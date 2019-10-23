# shows how a constructor is used in python
# __init__ is a constructor and it is used to initialize something we need for our object

class aPerson:

    # init methor aks constructor
    def __init__(self, name):
        self.name = name

    # a sample method
    def sayHi(self):
        print("Hello, my name is", self.name)

p = aPerson('Ankit Sharma')
p.sayHi()




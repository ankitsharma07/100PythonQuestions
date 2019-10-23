 /#!usr/bin/python3

class Pet:
    #__init__ is a constructor in Python
    def __init__(self, name, age):
        self.name = name
        self.age = age

#class Cat inheriting from class Pet
class Cat(Pet):
    def __init__(self, name, age):

        #calling the super-class function __init__
        super().__init__(name, age)


def main():
    thePet = Pet("Pet", 2)
    Bushy = Cat("Bushy", 3)

    #isInstance function to check if a class is inherited or not
    print("Is Bushy a cat? " + str(isinstance(Bushy, Cat)))
    print("Is Busy a pet? " + str(isinstance(Bushy, Pet)))
    print("Is the pet a cat? " + str(isinstance(thePet, Cat)))
    print("Is the pet a pet? " + str(isinstance(thePet, Pet)))
    print(Bushy.name)

if __name__ == '__main__':
    main()
    
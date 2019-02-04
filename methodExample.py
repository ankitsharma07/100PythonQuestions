#!usr/bin/python3

class vector2D:
    x = 0.0
    y = 0.0

    # creating a method named Set

    def Set(self, x, y):
        self.x = x
        self.y = y

def main():

    obj = vector2D()

    #Releasing values to the method using the dot operator
    obj.Set(2,3)

    print("X: " + str(obj.x) + ", Y: " + str(obj.y))

if __name__ == '__main__':
    main()
    
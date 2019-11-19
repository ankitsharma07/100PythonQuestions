#!usr/bin/python3

class myClass:
    #Assigning a value to the myClass attribute
    number = 0
    name = "noName"

def main():
    #Creating an object of the myClass

    iAmObject = myClass()

    #Accessing the attributes of myClass using the "dot" operator
    iAmObject.number = 122
    iAmObject.name = "Ankit Sharma"

    #Printing the output
    print(iAmObject.name + " " + str(iAmObject.number))

#Telling python that there is main function in the file::
if __name__ == '__main__':
    main()
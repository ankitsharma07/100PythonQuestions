# Class variable and instance variable

class CS_Student:

    # class variable
    stream = 'CSE'

    # init method
    def __init__(self, roll):

        # instance variable
        self.roll = roll

# Object of CS students
a = CS_Student(101)
b = CS_Student(102)

# Check for few things
print(a.roll)
print(a.stream)
print(b.roll)
print(b.stream)

class IT_Student:

    # class variable
    stream = 'IT'

    def __init__(self, roll):
        self.roll = roll

    def aboutAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address


c = IT_Student(111)
c.aboutAddress('Patna, Bihar, India')
print(c.stream)
print(c.roll)
print(c.getAddress())

d = IT_Student(112)
d.aboutAddress('Kanpur, UP, India')
print(d.stream)
print(d.roll)
print(d.getAddress())

e = IT_Student(113)
e.stream('Arts')
e.aboutAddress('Noida, UP')
print(e.stream)
print(e.roll)
print(e.getAddress())

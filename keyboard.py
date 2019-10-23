def keyboard(direction, string):
    keys = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    if direction == 'R':
        directionValue = -1
    elif direction == 'L':
        directionValue = 1

    msg = ""
    for i in string:
        msg = msg+keys[keys.find(i)+directionValue]
    return msg

direction = str(input())
string = str(input())

result = keyboard(direction, string)
print(result)

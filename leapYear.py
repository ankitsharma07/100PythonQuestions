#!/bin/python3

def leapYear(year):
    if year%4==0 or year%400==0:
        return True
    else:
        return False

if __name__=="__main__":
    y = int(input())
    check = leapYear(y)
    print(check)

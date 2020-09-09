import math


def convertToBase(num, base):
    stack = []
    while(num > 0):
        stack.insert(0, num % base)
        num = math.floor(num / base)

    return stack

import math

def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    # TODO: YOUR CODE HERE
    steps = 3 + 2 * math.ceil(n/5.0)
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    return y

print (countdown(50))
print (time(50))

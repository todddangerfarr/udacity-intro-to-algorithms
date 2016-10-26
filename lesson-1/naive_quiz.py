# Intro to Algorithms Naive Quiz
# What does the Naive Funciton do?

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

# run some examples
print("Running Naive with a = 2, and b = 6")
print(naive(2, 6)) # Outputs 12
print()
print("Running Naive with a = 4, and b = 8")
print(naive(4, 8)) # Outputs 32
print()
print("Running Naive with a = 30, and b = 25")
print(naive(30, 25)) # Outputs 750
print()
print("Running Naive with a = 7, and b = 11")
print(naive(7, 11)) # Outputs 77
print()

# naive is multiplying A and B

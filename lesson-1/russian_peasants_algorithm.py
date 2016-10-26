# Intro to Algorithms
# The Russian Peasants Algorithm for multiplication

def russian_peasants(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if (x % 2) == 1:
            z = z + y
        y = y << 1 # bit shifts
        x = x >> 1
    return z

# run some examples
print("Running Russian Peasants with a = 14, and b = 11")
print(russian_peasants(14, 11)) # Outputs 154
print()
print("Running Russian Peasants with a = 4, and b = 8")
print(russian_peasants(4, 8)) # Outputs 32
print()
print("Running Russian Peasants with a = 30, and b = 25")
print(russian_peasants(30, 25)) # Outputs 750
print()
print("Running Russian Peasants with a = 7, and b = 11")
print(russian_peasants(7, 11)) # Outputs 77
print()

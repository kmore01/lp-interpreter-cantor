import math

# Cantor's pairing function
def pi(x, y):
    return (x + y) * (x + y + 1) // 2 + y

# Inverse of the Cantor function
def unpi(z):
    w = math.floor((math.sqrt(8 * z + 1) - 1) / 2)
    t = (w * w + w) // 2
    y = z - t
    x = w - y
    return x, y

# Function for encoding inputs
def encode_input(entrada):
    elements = entrada.split()
    if not elements:
        return 0
    nums = [int(n) for n in elements]

    result = nums[-1]  # Last number
    # We apply pi from right to left with the remaining elements
    for num in reversed(nums[:-1]):  # nums[:-1] list without the last
        result = pi(num, result)
    return result

# Constant function 1
def k_1(z):
    return 1

# Identity function
def id(z):
    return z

# Function that given a pair <x,y> returns x + y
def add(z):
    x, y = unpi(z)
    return x + y

# Function that given a pair <x, y> returns x * y
def mul(z):
    x, y = unpi(z)
    return x * y

# Function that given a pair <x, y> returns max(0, x - y)
def diff(z):
    x, y = unpi(z)
    return max(0, x - y)
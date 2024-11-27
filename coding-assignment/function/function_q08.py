#8. Find the LCM (Least Common Multiple)
Write a function that calculates the Least Common Multiple (LCM) of two numbers.

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(lcm(15, 20))

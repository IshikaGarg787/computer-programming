#7. Find the GCD (Greatest Common Divisor)
#Write a function that finds the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(56, 98))

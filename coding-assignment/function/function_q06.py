#6. Fibonacci Sequence
#Write a function that returns the nth number in the Fibonacci sequence.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

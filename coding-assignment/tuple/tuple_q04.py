#4. Create a Tuple from User Input
#Problem: Create a tuple from user input, e.g., "10 20 30".

user_input = input("Enter numbers separated by space: ")
t = tuple(map(int, user_input.split()))
print(t)

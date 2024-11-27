#4. Check if a String is a Valid Email Address
#Problem: Check if the string "example@example.com" is a valid email address (simple validation).

s = "example@example.com"
print("@" in s and "." in s.split("@")[-1])


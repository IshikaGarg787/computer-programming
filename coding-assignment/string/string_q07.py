#7. Find All Substrings of Length N
#Problem: Find all substrings of length 3 in the string "abcdef".

s = "abcdef"
n = 3
substrings = [s[i:i+n] for i in range(len(s) - n + 1)]
print(substrings)

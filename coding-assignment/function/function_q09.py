#9. Count Vowels in a String
#Write a function that counts the number of vowels in a string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello world"))

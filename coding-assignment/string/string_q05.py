#5.Find the Longest Word in a String
#Problem: Find the longest word in the string "The quick brown fox jumped over the lazy dog".

s = "The quick brown fox jumped over the lazy dog"
words = s.split()
longest_word = max(words, key=len)
print(longest_word)


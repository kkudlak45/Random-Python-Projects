# Kryzstof Kudlak
# 7/15/18
# 6.00.1x - Vowel Counter

s = "this is some kind of string"
vowels = 0

def checkVowels(l):
    if (l == "a" or l == "e" or l == "i" or l == "o" or l == "u"):
        return True
    else:
        return False

for x in range (len(s)):
    if (checkVowels(s[x])):
        vowels = vowels + 1

print("The string is " + str(s))
print("This string has: " + str(vowels) + " vowels")
        
    

# Kryzstof Kudlak
# 7/15/18
# 6.00.1x - Alphabetical Strings

s = 'azcbobobegghakl'

long = "a"
new = s[0]

for i in range (len(s)):
    if (ord(new[len(new)-1]) <= ord(s[i])):
        if (i == 0):
            new = s[i]
        else:
            new = new + s[i]
    elif (ord(new[len(new)-1]) > ord(s[i])):
        if (len(new) > len(long)):
            long = new
            new = s[i]
        elif (len(new) <= len(long)):
            new = s[i]

print("Longest substring in alphabetical order is: " + str(long))

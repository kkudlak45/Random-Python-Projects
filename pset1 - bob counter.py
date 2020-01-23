# Kryzstof Kudlak
# 7/15/18
# 6.00.1x - Bob Counter

s = 'bobboobobobbbobhbobbgobooobbooboobobobb'
bobs = 0

def checkBob(pos):
    if (pos + 2 < len(s)):
        if (s[pos + 1] == "o" and s[pos + 2] == "b"):
            return True

for i in range (len(s)):
    if (s[i] == "b" and checkBob(i)):
        bobs = bobs + 1

print("Number of times 'bob' occurs is: " + str(bobs))
    

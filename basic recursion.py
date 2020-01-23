# Kryzstof Kudlak
# 7/17/18
# Recursion Concept

def fact(num):
    if (num > 1):
        return num * fact(num - 1)
    elif (num == 1):
        return num


print(fact(10))

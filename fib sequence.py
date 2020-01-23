# Kryzstof Kudlak
# 7/17/18
# CMU Recursion Practice Prob 2

s = [1, 1]
num = int(input("Which number in sequence?"))
n = 2

while (n < num):
    s.append(s[n-2] + s[n-1])
    n = n + 1

print(s[len(s) - 1])

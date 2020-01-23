# Kryzstof Kudlak
# 7/7/18
# Bubble Sort Function


x = [35, 6575, 1324, 3, 235, 432, 12, 354, 2, 57]

n = len(x)
for ___ in range (n - 1):
    for i in range(n - 1):
        if (x[i] > x[i + 1]):
            x[i],x[i+1] = x[i+1],x[i]
            
print(x)




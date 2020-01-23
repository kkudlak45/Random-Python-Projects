# Kryzstof Kudlak
# 7/17/18
# CMU Recursion Practice Prob 1

def main():
    # compute and print 1 + 2 + ... + 10
    print(sum(10))

def sum(x):
    if (x > 1):
        return x + sum(x - 1)
    elif (x == 1):
        return x

    
main()

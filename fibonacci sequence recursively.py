# Kryzstof Kudlak
# 7/17/18
# CMU Recursion Practice Prob 2

def main():
    n = 2
    num = input("Which number in the sequence?")
    for i in range (10):
        fib(1, 1)

def fib(first, second):
    return fib(second, first + second)
    
main()

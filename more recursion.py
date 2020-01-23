# Kryzstof Kudlak
# CMU Practice Problem 3
# 7/17/18

def main():
    print(dig(15))
    print(dig(105))
    print(dig(15105))

def dig(n):
    if (n < 10):
        return 1 # return number of digits in the last number
    else:
        return 1 + dig(n/10) # return 1 + number of digits in the next number

main()

n = 140

def divisible(num):
    if (num%19 == 0):
        if (num%17 == 0):
            if (num%13 == 0):
                if (num%11 == 0):
                    if (num%18 == 0):
                        if (num%15 == 0):
                            if (num%12 == 0):
                                if (num%16 == 0):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


while (divisible(n) == False):
    n = n + 140

print(n)

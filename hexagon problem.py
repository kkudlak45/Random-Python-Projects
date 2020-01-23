n = 202
r = n - 1
l = n - 1


def nex(ri):
    if (ri == n + 2):
        return n + 2
    else:
        return ri + nex(ri + 1)

def nexx(ri):
    if (ri == n + 1):
        return n + 1
    else:
        return ri + nexx(ri + 1)
    
print(nex(r) + nexx(l))

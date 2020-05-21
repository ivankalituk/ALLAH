def inc(m):
    n = int(input())

    if n == 0:
        return m
    else:
        m.append(n)
        return inc(m)

def outc(m,n):
    if n == -1:
        return(m[0])
    else:
        print(m[n], end = ' ')
        return outc(m,n-1)


m = []

m = inc(m)
n = len(m)-1

n = outc(m,n)

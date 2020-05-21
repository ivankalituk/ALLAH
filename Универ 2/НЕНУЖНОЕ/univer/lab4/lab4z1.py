def arp (a1,n,d):
    if n == 0:
        return a1
    else:
        a1 = a1 + d
        return arp(a1, n-1,d)


a1 = int(input())
n = int(input())
d = int(input())
i = 1
an = arp(a1,n-1,d)
print(an)
s = (a1 + an)/2*n
print(s)

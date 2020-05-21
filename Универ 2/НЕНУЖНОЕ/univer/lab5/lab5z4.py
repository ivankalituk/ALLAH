def ifn(s,n):
    sp = ''
    i = 1
    if s[n] =='<':
        while s[n+i] != '>':
            sp = sp + s[n+i]
            i = i + 1
    return sp




s = input()
n = 0

print(ifn(s,n))





def ifn(s,n):
    while s[n] != '<':
        n = n + 1
    while s[n] != '>':
        

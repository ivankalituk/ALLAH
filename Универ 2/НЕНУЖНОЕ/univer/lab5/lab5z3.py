def findn(s,i,n):
    if i == len(s):
        return n
    else:
        if (s[i]=='0')or(s[i]=='1')or(s[i]=='2')or(s[i]=='3')or(s[i]=='4')or(s[i]=='5')or(s[i]=='6')or(s[i]=='7')or(s[i]=='8')or(s[i]=='9'):
            n = n + 1
        return(findn(s,i+1,n))

for i in range(5):
    s = input('s = ')
    n = 0
    i = 0
    print(findn(s,i,n))

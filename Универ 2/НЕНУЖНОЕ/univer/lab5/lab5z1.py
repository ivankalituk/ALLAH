def fact(f,i,n):
    if i == n:
        return f
    else:
        f = f * i
        return(fact(f,i+1,n))


n = int(input('n = ')) + 1
i = 1
f = 1



print(fact(f,i,n))

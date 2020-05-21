import random

def ma(m,maximum,ind,n):
    if n == len(m):
        return ind
    else:
        if m[n] >= maximum:
            maximum = m[n]
            ind = n
        return(ma(m,maximum,ind,n+1))


    


n = int(input('n = '))
m = []

for i in range(n):
    m.append(random.randint(0,20))
    
for i in range(n):
    print(m[i], end = ' ')
print()

n = 0
maximum = -1
ind = -1
print(ma(m,maximum,ind,n))

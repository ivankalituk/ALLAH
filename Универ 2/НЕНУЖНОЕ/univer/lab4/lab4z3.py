def nn(m,i,n):
    if i == n:
        return 1
    else:
        print(m[i])
        return nn(m,i+1,n)


n = int(input('n = '))
m = []

for i in range(10):
    for j in range(i):
        m.append(i)

for i in range(len(m)):
    print(m[i], end = ' ')
print()        
i = 0
n = nn(m,i,n)

import random

def isPower(k):
    i = 0
    a = 0
    while (i**5 <= k):
        i = i + 1
        if k  == i**5:
            a = 1

    if a == 1:
        return(1)
    else:
        return(0)


m = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(m)):
    m[i]= random.randint(0,100)

for i in range(len(m)):
    print (m[i], end = " ")
print()

#m[2] = 32
#m[4] = 1

for i in range(len(m)):
    print(isPower(m[i]), end = " ")

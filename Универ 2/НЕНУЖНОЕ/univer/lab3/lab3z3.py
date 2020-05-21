import random

m = [0,0,0,0,0,0,0,0,0,0]
min = 100

for i in range(len(m)):
    m[i]= random.randint(0,100)

for i in range(len(m)):
    print (m[i], end = " ")
    if m[i] < min:
        min = m[i]
print()


while m[0] != min:
    f = m[0]
    for i in range(len(m)-1):
        m[i] = m[i+1]
    m[len(m)-1] = f

for i in range(len(m)):
    print (m[i], end = " ")
print()

import random

m = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]= random.randint(0,100)
        
for i in range(len(m)):
    for j in range(len(m)):
        print(m[i][j], end = " ")
    print()

print()

for i in range(len(m)):
    for j in range(len(m)):
        m[i][j] = m [i][j] - m[2][j]

for i in range(len(m)):
    for j in range(len(m)):
        print(m[i][j], end = " ")
    print()

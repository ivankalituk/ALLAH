def vyz(m):
    a1 = m[0][0] + m[1][1] + m[1][1]
    a2 = m[2][0] + m[0][2] + m[1][2]
    a3 = m[0][2] + m[1][0] + m[2][1]

    a4 = m[2][0] + m[1][1] + m[0][2]
    a5 = m[0][0] + m[1][2] + m[2][1]
    a6 = m[2][2] + m[1][0] + m[0][1]
    return a1+a2+a3-a4-a5-a6



import random

m = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]= random.randint(0,10)
        
for i in range(len(m)):
    for j in range(len(m)):
        print(m[i][j], end = " ")
    print()

print(vyz(m))

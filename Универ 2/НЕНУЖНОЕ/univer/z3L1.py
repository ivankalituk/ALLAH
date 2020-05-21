x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

ab = ((x1-x2)**2+(y1-y1)**2)**0.5
ba = ((x2-x2)**2+(y1-y2)**2)**0.5

print(2*ab+2*ba)
print(ab*ba)

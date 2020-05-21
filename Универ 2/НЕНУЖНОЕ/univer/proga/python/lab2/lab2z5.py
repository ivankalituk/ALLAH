import math
e = input('введите количество элементов ')

e = int(e)
a = 1
b = 2


while math.fabs(a - b) >= e:
    c = b
    b = (a + 2 * b)
    a = c

print(a)
print(b)

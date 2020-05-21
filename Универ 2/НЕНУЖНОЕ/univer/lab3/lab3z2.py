def nsk (a,b):
    i = a
    while (i % a != 0) or (i % b != 0):
        i = i + 1
    return(i)


a = int(input('a = '))
b = int(input('b = '))

print(nsk(a,b))

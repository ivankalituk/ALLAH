n = input('введите число ')

n = int(n)

if n == 0:
    print('нулевой')
elif n > 0:
    if n % 2 == 0:
        print('положительный, парный')
    else:
        print('положительный, непарный')
else:
     if n % 2 == 0:
        print('отрицательный, парный')
     else:
        print('отрицательный, непарный')

def hard():
    m = []
    n = int(input())
    m.append(n)
    if n == 0:
        return max
    else:
        if len(m) > 1:
            if m[len(m)-1] <=m[len(m)]:
                max = m[len(m)]
            else:
                max = m[len(m)]
        return hard()

print(hard())

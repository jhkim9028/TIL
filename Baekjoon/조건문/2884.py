h, m = map(int, input().split())

if m >= 45:
    y = m - 45
    x = h
else:
    y = m + 15
    if h == 0:
        x = 23
    else:
        x = h - 1

print(x, y)
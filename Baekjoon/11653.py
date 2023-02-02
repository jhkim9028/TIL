N = int(input())

a = 2

while True:
    if not N % a:
        print(a)
        N = N // a
    elif N % a:
        a += 1
    if N < a:
        break
        
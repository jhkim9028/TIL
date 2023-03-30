import sys
input = sys.stdin.readline

T = int(input())



for t in range(T):
    q = 0
    d = 0
    n = 0
    p = 0
    
    money = int(input())
    while True:
        if money - 25 <0:
            break
        money -= 25
        q += 1
    while True:
        if money - 10 <0:
            break
        money -= 10
        d += 1
    while True:
        if money - 5 <0:
            break
        money -= 5
        n += 1
    while True:
        if money - 1 <0:
            break
        money -= 1
        p += 1
    print(q,d,n,p)
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab = {}
for i in range(len(A)):
    ab[A[i]] = B[i]
#print(ab) #{4: 1, 5: 2, 6: 3, 7: 4, 0: 5, 1: 6, 2: 7, 3: 8, 9: 9, 8: 0}

a = 0
b = 0
d = 0
ls = []
for k , v in ab.items():
    if k > v:
        a += 3
        ls.append('A')
    elif v > k:
        b += 3
        ls.append('B')
    elif k == v:
        a += 1
        b += 1
        d += 1
        
print(a,b)
if a > b:
    print('A')
elif b > a:
    print('B')
elif a == b:
    if d == 10:
        print('D')
    elif ls[-1] == 'A':
        print('A')
    else:
        print('B')
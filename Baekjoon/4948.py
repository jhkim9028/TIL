import sys
input = sys.stdin.readline

ar = 123456 * 2

arr = [True,True] + [True] * (ar-1)

for i in range(2, int(ar**0.5)+1):
    if arr[i]:
        for j in range(2*i,ar+1,i):
            arr[j] = False


while True:
    num = int(input())
    cnt = 0
    if not num:
        break
    
    for i in range(num+1,2*num+1):
        if arr[i]:
            cnt += 1

    
    print(cnt)

    
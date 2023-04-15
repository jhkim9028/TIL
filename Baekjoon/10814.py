import sys
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(201)]

for i in range(N):
    age, name = map(str, input().split())
    arr[int(age)].append(name)

for j in range(len(arr)):
    if arr[j]:
        if len(arr[j]) == 1:
            print(j, *arr[j])
        else:
            for k in range(len(arr[j])):
                print(j, arr[j][k])
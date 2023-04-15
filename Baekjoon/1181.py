import sys
input = sys.stdin.readline

N = int(input())

arr = []


for _ in range(N):
    word = input().rstrip()
    if word not in arr:
        arr.append(word)
    
arr.sort()
array = sorted(arr, key=lambda x : len(x))

for i in range(len(array)):
    print(array[i])
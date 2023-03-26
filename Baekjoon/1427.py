import sys
input = sys.stdin.readline

num = input()
arr = [0] * 10
for i in range(len(num)-1):
    arr[num[i]] += 1


ans = []
for j in range(10):
    if arr[j] > 0:
        ans.append(f'{j}'*arr[j])

print(ans)
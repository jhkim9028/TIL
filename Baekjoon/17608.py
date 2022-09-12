N = int(input())
list_ = []
cnt = 0
max = 0
for n in range(N):
    list_.append(int(input()))

for num in list_[::-1]:
    if max < num:
        max = num
        cnt += 1
print(cnt)
# 아니 똑같은데 위에는 안되고 밑에는 되는건데;;;;;;;;;;;;;
import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
	l.append(int(input()))
count = 0
max = 0
for x in reversed(l):
	if max < x:
		max = x
		count += 1
print(count)
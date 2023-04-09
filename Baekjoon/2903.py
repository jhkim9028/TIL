n = int(input())

dot = 2
cnt = 2

for i in range(n):
    dot += cnt**i

print(dot*dot)
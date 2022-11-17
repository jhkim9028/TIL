import sys

number = []
for i in range(30):
    number.append(i+1)
for j in range(28):
    number.remove(int(sys.stdin.readline().strip()))
for x in number:
    print(x)
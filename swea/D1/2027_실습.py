import sys

sys.stdin = open("2027_input.txt", "r")

for i in range(5):
    for j in range(5):
        if i == j:
            print('#',end='')
        else:
            print('+', end='')
    print()
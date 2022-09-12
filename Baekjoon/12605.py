import sys
sys.stdin = open('12605_input.txt')

N = int(input())

for n in range(N):
    sen = list(input().split())
    new = ''
    for s in reversed(sen):
        new += s
        new += ' '
    print(f'Case #{n+1}: {new}')
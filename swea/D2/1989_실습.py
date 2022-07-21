import sys

sys.stdin = open("1989_input.txt", "r")

T = int(input())

for i in range(1,T+1):
    word = input()
    if  word == word[::-1]:
        print(f'#{i} {1}' )
    else:
        print(f'#{i} {0}' )
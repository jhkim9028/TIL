import sys

sys.stdin = open("10798_input.txt", "r")

new = []
min_len = 10
for t in range(5):
    word = list(input())
    if len(word) < min_len:
        min_len = len(word)
    new.append(word)

ans = ''
for i in range(min_len):
    for j in range(5):
        print(ans + new[j][i],end='')
        

for i in range()
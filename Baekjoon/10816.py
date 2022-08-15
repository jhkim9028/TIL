import sys
sys.stdin = open('10816_input.txt')

from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int, stdin.readline().split()))

m = stdin.readline().rstrip()
num = list(map(int, stdin.readline().split()))

num_dict = {}
for n in num:
    num_dict[n] = 0

card_dict = {}
for c in card:
    card_dict[c] = 0

for c in card:
    card_dict[c] += 1

for n in num:
    if n not in card_dict.keys():
        print(0,end=' ')
    else:
        print(card_dict.get(n), end=' ')


import sys

sys.stdin = open("2711_input.txt", "r")

t = int(input())

for i in range(t):
  ota, word = input().split()
  for w in range(1):
    print(word[:int(ota)-1] + word[int(ota):])
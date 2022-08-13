import sys
sys. stdin = open('9093_input.txt')

T = int(input())


for t in range(T):
    new = []
    sentence = list(input().split())
    for i in range(len(sentence)):
        
        new.append(sentence[i][::-1])
    print(*new)
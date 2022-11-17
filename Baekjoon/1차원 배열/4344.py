import sys
sys.stdin = open('4344_input.txt')

T = int(input())

for t in range(T):
    score = list(map(int, input().split()))
    cnt = 0
    avg = sum(score[1::])/score[0]
    for s in score[1::]:
        if s > avg:
            cnt += 1
    print("{:.3f}%".format(100*cnt/score[0]))
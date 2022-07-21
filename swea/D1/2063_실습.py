import sys

sys.stdin = open("2063_input.txt", "r")

T = int(input())

# T개만큼 점수를 입력한다.
# list에 점수들 담고 정렬 후에 T를 2로 나눈 몫은 중간
N = list(map(int, input().split()))
N.sort()
a = T // 2
print('{}'.format(N[a]))
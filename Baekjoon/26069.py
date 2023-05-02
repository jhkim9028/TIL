import sys
input = sys.stdin.readline

T = int(input())

chong = 'ChongChong'

dance = []

for t in range(T):
    man1, man2 = map(str, input().split())

    if man1 == chong or man2 == chong:
        if man1 not in dance:
            dance.append(man1)
        if man2 not in dance:
            dance.append(man2)
        continue

    if man1 in dance or man2 in dance:
        if man1 not in dance:
            dance.append(man1)
        if man2 not in dance:
            dance.append(man2)
print(len(dance))
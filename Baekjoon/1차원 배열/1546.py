n = int(input())
score = list(map(int, input().split()))

max_ = max(score)
new_score = []

for s in score:
    new_score.append(s/max_*100)
print((sum(new_score))/n)
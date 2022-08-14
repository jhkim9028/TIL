n = 0
sangsung = set()
a = []
while n != 10000:
    n += 1
    new = 0
    sum_ = 0
    a.append(n)
    for i in str(n):
        new += int(i)
    sum_ = n + new
    sangsung.add(sum_)
for j in a:
    if j not in sangsung:
        print(j)
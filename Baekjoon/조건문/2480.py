num = list(map(int, input().split()))

ans = 0

if num.count(num[0]) == 3:
    ans = 10000 + num[0] * 1000
elif num.count(num[0]) == 1 and num.count(num[1]) == 1:
    ans = max(num) * 100
elif num.count(num[0]) == 2:
    ans = 1000 +num[0] * 100
elif num.count(num[1]) == 2:
    ans = 1000 + num[1] * 100
elif num.count(num[2]) == 2:
    ans = 1000 + num[2] * 100
    
print(ans)
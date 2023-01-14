# 9613

# 각 쌍마다 최대공약수를 구해서 합을 구한다

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


T = int(input())

for t in range(T):
    num = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(num)):
        for j in range(1, len(num)):
            if i < j:
                ans += gcd(num[i],num[j])
            else:
                pass
    print(ans)
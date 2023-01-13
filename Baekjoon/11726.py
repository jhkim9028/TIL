# 11726

# 2 * n 크기의 직사각형에 1 * 2, 2 * 1 크기 타일로 채우는 방법의 수
# 규칙 : n = 4 = (n = 3) + (n = 2)


n = int(input())
# 1 <= n <= 1000

N = 0
a = 1
ans = [1,2]
# n=1일 때 1, n=2일 때 2


for i in range(2,1000):
    ans.append(ans[i-1]+ans[i-2])

print(ans[n-1] % 10007)
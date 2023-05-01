import sys
input = sys.stdin.readline

def gcd_(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = gcd_(gcd,item)
    return gcd

T = int(input())

# 가로수
trees = []

# 가로수 사이 간격
space = []
for t in range(T):
    tree = int(input())
    trees.append(tree)
    if t > 0:
        space.append(tree - trees[t-1])

# 공차 = space의 최대공약수
spaceD = int(gcd_N(space))

# 총 개수
totalCnt = int((trees[-1] - trees[0] + spaceD) / spaceD)
print(totalCnt - T)
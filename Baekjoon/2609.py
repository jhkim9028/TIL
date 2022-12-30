# 2609

A, B = map(int, input().split())

# 약수
A_ = []
B_ = []
# 공통 약수
a = []
for i in range(1,A+1):
    if A % i == 0:
        A_.append(i)
        
for j in range(1,B+1):
    if B % j == 0:
        B_.append(j)
        
for k in A_:
    if k in B_:
        a.append(k)
        
# 최소공배수 
ans = (A / max(a)) * (B / max(a)) * max(a)

print(max(a))
print(int(ans))
S = input()

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]


ans = []

for i in alphabet:
    if i in S:
        ans.append(S.find(i))
    else:
        ans.append(-1)
print(*ans)
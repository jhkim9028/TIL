H, M = map(int, input().split())
plus = int(input())

new_H = H + (M + plus) // 60
plus_M = M + plus 


if plus_M <= 59:
    print(H, plus_M)
else:
    if new_H > 23:
        print(new_H-24, plus_M - ((plus_M // 60)*60))
    else:
        print(new_H, plus_M - ((plus_M // 60)*60))
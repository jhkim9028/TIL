nums = []
max_num = []
for i in range(9):
    num = list(map(int, input().split()))
    max_num.append(max(num))
    nums.append(num)

x = max_num.index(max(max_num))


for i in range(9):
    if nums[x][i] == max(max_num):
        y = i

print(max(max_num))
print(x+1,y+1)
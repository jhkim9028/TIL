tb = input()

count = 0
left = 0
for i in tb:
    if i == '@':
        count += 1
    elif i == "(":
        left = count
        count = 0
    elif i == '@':
        count += 1
print(left, count)
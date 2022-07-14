numbers = [0, 20, 100]

mid = numbers[0]

for i in numbers:
    if  mid < i:
        mid = i

print(mid)
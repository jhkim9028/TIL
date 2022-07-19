numbers = [0, 20, 100, 40]

max = numbers[0]
second = numbers[0]

for i in numbers:
    if max < i:        
        second = max
        max = i  
    elif second < i and i < max:
        second = i
print(second)
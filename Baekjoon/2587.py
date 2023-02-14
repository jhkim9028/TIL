avg = []
center = []

for i in range(5):
    num = int(input())
    avg.append(num)
    

print(int(sum(avg) / 5))

avg.sort()
print(avg[2])
    
    
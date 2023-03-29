import sys
input = sys.stdin.readline

score = []
total = 0
for i in range(20):
    sub = input().split()
    
    if sub[-1] == 'P':
        continue
    
    if sub[-1] == 'A+':
        a = 4.5
    elif sub[-1] == 'A0':
        a = 4.0
    elif sub[-1] == 'B+':
        a = 3.5
    elif sub[-1] == 'B0':
        a = 3.0
    elif sub[-1] == 'C+':
        a = 2.5
    elif sub[-1] == 'C0':
        a = 2.0
    elif sub[-1] == 'D+':
        a = 1.5
    elif sub[-1] == 'D0':
        a = 1.0
    elif sub[-1] == 'F':
        a = 0.0
    score.append(a * float(sub[1]))
    total += float(sub[1])
    

print(sum(score)/total)



import sys
sys.stdin = open('1076_input.txt')

color = {
    'black' : '0',
    'brown' : '1',
    'red' : '2',
    'orange' : '3',
    'yellow' : '4',
    'green' : '5',
    'blue' : '6',
    'violet': '7',
    'grey' : '8',
    'white' : '9' 
}

color_list = [input() for _ in range(3)]
a = []
for i in range(len(color_list)):
    a.append(color[color_list[i]])
ans = ''
total = 0
for j in range(len(a)):
    if j == 2:
        total = int(ans) * 10**int(a[j])
    else:
        ans += a[j]

print(total)
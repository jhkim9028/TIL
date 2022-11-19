word = input()

cro = [
    'c=',
    'c-',
    'dz=',
    'd-',
    'lj',
    'nj',
    's=',
    'z='
]
for c in cro:
    word = word.replace(c,'1')

cnt = 0
for w in word:
    cnt += 1
    
print(cnt)
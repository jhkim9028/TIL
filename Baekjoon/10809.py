s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    if a in s:
        print(s.find(a),end=' ')
    else:
        print(-1,end=' ')
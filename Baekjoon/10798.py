from dataclasses import replace
import sys


import sys

sys.stdin = open("10798_input.txt", "r")

w = []
a = input()
a = list(a)
b = input()
b = list(b)
c = input()
c = list(c)
d = input()
d = list(d)
e = input()
e = list(e)
for i in range(len(a)):
    if len(a) != len(a):
        a.append(\)
    if len(b) != len(a):
        b.append(' ')
    if len(c) != len(a):
        c.append(' ')
    if len(d) != len(a):
        d.append(' ')
    if len(e) != len(a):
        e.append(' ')
for i in range(len(a)):
    w.append(a[i])
    w.append(b[i])
    w.append(c[i])
    w.append(d[i])
    w.append(e[i])
#print(w)
k = ''
for i in w:
    k += i
k.replace(' ','')
print(k, end='')
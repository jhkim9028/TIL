import sys
sys.stdin = open('10951_input.txt')

try:
    while True:
        a, b = map(int, input().split())
        print(a+b)
except:
    pass
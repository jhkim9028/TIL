import sys

sys.stdin = open("2029_input.txt", "r")

T = int(input())
for i in range(1,T+1):
    a, b = map(int, input().split())
    print('#',i, a//b, a%b)
    
# T = int(input())
# for tt in range(T):
#     a, b = map(int, input().split())
#     print( "#%d %d %d" % (tt+1, a//b, a%b) )
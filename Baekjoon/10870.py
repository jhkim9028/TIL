import sys
input = sys.stdin.readline



a = 0 #1
b = 1 #2
number = int(input())
number2 = number // 2
def Fibonacci(num):
    global a
    global b
    if num == 0:
        return a, b

    a += b
    b += a
    return Fibonacci(num - 1)

ans = Fibonacci(number2)
if number % 2 == 1:
    print(ans[1])
else:
    print(ans[0])
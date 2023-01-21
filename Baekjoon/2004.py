# n! / m! * (n - m)!

def count_num(a, b):
    
    cnt = 0
    while a != 0:
        a = a // b
        cnt += a
    return cnt

N, M = map(int, input().split())

count_2 = count_num(N,2) - count_num(M, 2) - count_num(N-M, 2)
count_5 = count_num(N,5) - count_num(M, 5) - count_num(N-M, 5)

print(min(count_2, count_5))
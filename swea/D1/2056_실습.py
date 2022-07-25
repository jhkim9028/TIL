import sys

sys.stdin = open("2056_input.txt", "r")

T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 월별 일수를 리스트로 만든다.

# 월별 자리의 조건이 맞는지 보고 맞으면 
# 입력값의 마지막 두 자리가 일수와 맞는지 비교한다. 

# 모든 조건이 만족하면 /를 추가해서 출력한다.
# /는 어떻게 추가해야 하나??

# 조건이 불만족하면 -1 출력


for i in range(1, T+1):
    num_str = input()
    year = num_str[0:4]
    mon = num_str[4:6]
    day = num_str[6:]
    # print(year, mon, day) 잘 나눠짐
    while True:
        # if 를 따로 두번 하자
        if int(mon) == 0 or int(mon) >= 13:
            print(f'#{i} -1')
            break
        elif int(day) <= 0 or int(day) > days[int(mon)-1]:
            print(f'#{i} -1')
            break
        else:
            print('#%01d %04d/%02d/%02d' %(i, int(year), int(mon), int(day)))
            print(f'#{i} {year}/{mon}/{day}')
            break
            
        
# 두 자리수 => 자리별로 나눠서 뒤에 자리 수를 앞자리로 보내고 더한 값을 뒷자리로 보내서
# 하나의 수로 만듬 이 과정을 반복해서 처음 수로 나오는게 몇 번째인지 출력
# 10보다 작은 수는 앞에 0을 붙여서 진행

#26

N = input()
if int(N) < 10:
    N = '0' + N
sum_ = 0 # 앞자리 뒷 자리 더한 값
sum_num = N[0] + N[-1]# 뒷 자리 + sum_의 뒷 자리
cnt = 0
while True:
    sum_ = int(sum_num[0]) + int(sum_num[1])
    sum_num = sum_num[-1] + str(sum_)[-1]
    cnt += 1
    if sum_num == N:
        break
print(cnt)
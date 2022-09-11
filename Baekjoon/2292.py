# 1,6,12,18
# 2칸 : 6개
# 3칸 : 12개
# 4칸 : 18개
# 5칸 : 24개

n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)
# 4375

# 2와 5로 나누어떨어지지 않는 정수 n
# 1로만 이루어진 n의 배수중 가장 작은 수의 자리수





while True:
    try: 
        n = int(input())
        a = '1'
        cnt = 1 
        while True:
            if int(a) % n == 0:
                print(cnt)
                break
            else:
                a = a + '1'
                cnt += 1
    except:
        break
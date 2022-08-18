# import sys
# sys.stdin = open('20001_input.txt')

moon = []
while True:
    duck = input()
    if duck == '고무오리 디버깅 시작':
        continue
    elif duck == '문제':
        moon.append(duck)

    if duck == '고무오리':
        if len(moon) == 0:
            moon.append('문제')
            moon.append('문제')

        else:
            moon.pop()

    if duck == '고무오리 디버깅 끝':
        if len(moon) == 0:
            print('고무오리야 사랑해')
            break
        else:
            print('힝구')
            break
        
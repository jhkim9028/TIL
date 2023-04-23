import sys
input = sys.stdin.readline

sugar = int(input())

bag = 0

while sugar >=0:
    if sugar % 5 == 0:
        cnt5 = sugar // 5
        bag += cnt5
        print(bag)
        break
    
    sugar -= 3
    bag += 1

else:
    print(-1)


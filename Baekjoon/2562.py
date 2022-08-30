import sys
sys.stdin = open('2562_input.txt')

max_num = 0
number = []
for n in range(9):
    num = int(input())
    number.append(num)
for i in range(len(number)):
    if number[i] == max(number):
        print(max(number))
        print(i+1)

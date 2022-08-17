import sys
imput = sys.stdin.readline



card_dic = {}
for _ in range(int(input())) :
    card = int(input())
    if card in card_dic :
        card_dic[card] += 1
    else :
        card_dic[card] = 1
a = 0

for k, v in sorted(card_dic.items()):
    if v == max(card_dic.values()):
        a = k
        break
print(a)
    

        

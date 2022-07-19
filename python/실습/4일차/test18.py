word =input()

my_dict = {}

for i in word:
    my_dict[i] = 0
    for k in word:
        if k == i:
            my_dict[k] += 1

for j in my_dict:
    print(j, my_dict[j])
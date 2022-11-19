word = input()

new_word = word.upper()

set_word = set(new_word)

dict_ = {}

for s in set_word:
    dict_[s] = new_word.count(s)
a = sorted(dict_.values())[::-1]

for k, v in dict_.items():
    if len(a) >= 2:    
        if a[0] == a[1]:
            ans = '?'
        else:
            if v == max(dict_.values()):
                ans = k
    else:
        ans = k
    
print(ans)
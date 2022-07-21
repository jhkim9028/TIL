word = 'apple'
#print(word[::-1])

new_word = ''
for i in range(len(word)):
    new_word = word[len(word)-(i+1)]
    print(new_word, end='')

#for i in word:
#    new_word = char + new_word
#print(new_word)

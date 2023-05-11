import sys
input = sys.stdin.readline

wordsCnt, limit = map(int, input().split())

words = {}

for i in range(wordsCnt):
    word = input().rstrip()
    
    if len(word) < limit:
        continue

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

newWords = sorted(words.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))

for n in newWords:
    print(n[0])
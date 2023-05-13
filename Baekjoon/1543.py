import sys
input = sys.stdin.readline

document = input().strip()
documentList = list(document)
word = input().strip()
cnt = 0


n = 0
m = len(word)
while True:
    if n > len(document)- len(word):
        break
    
    if document[n:m] == word:
        cnt += 1
        n += len(word)
        m = n + len(word)
        continue
    n += 1
    m += 1
    
print(cnt)
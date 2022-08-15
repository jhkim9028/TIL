import sys
sys.stdin = open('1302_input.txt')

N = int(input())
books = {}
b = []
for n in range(N):
    book = input()
    b.append(book)
    books[book] = 0

ans = []
for i in b:
    books[i] += 1

for k, v in books.items():
    if v == max(books.values()):
        ans.append(k)
ans.sort()
print(ans[0])

    
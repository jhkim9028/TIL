word = 'CAMBRIDGE'

mail = input()
ans = []
for i in word:
    if i in mail:
        mail = mail.replace(i,'')
print(mail)
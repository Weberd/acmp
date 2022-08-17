b = input()
a = "qwertyuiopasdfghjklzxcvbnmq"

for i in range(len(a)):
    if b == a[i]:
        print(a[i + 1 - len(a)])
        break

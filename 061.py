a = b = 0
for i in range(4):
    c, d = map(int, input().split())
    a += c
    b += d

if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print('DRAW')
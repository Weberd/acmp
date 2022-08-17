n = int(input())
s = 1

# 1 + 2 + 3 + 6 = 12

for i in range(2, n + 1):
    if n % i == 0:
        s += i

print(s)
n = int(input())
a = []

for i in range(n):
    a.append(map(int, input().split()))

for i in a:
    n, m = i
    print(19 * m + (n + 239) * (n + 366) // 2)
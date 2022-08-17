import math

k, n = map(int, input().split())

page = int(math.ceil(n / k))
onpage = n - (n // k) * k

if onpage == 0:
    onpage = k

print(page, onpage)

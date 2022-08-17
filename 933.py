a, b, c, t = map(int, input().split())

if t <= a:
    print(b * t)
else:
    print((t - a) * c + a * b)
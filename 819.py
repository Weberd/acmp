a, b, c = map(int, input().split())

v = a * b * c
s = a * b * 2 + a * c * 2 + b * c * 2

print(s, v)
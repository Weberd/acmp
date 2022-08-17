import math

l, w, h = map(int, input().split())

s = math.ceil((l * h * 2 + w * h * 2) / 16)
print(s)

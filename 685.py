a1, a2, a3, b1, b2, b3 = map(int, input().split())
a = [a1, a2, a3]
b = [b1, b2, b3]
a.sort()
a.reverse()

b.sort()
b.reverse()

c = sum([d * e for d, e in zip(a, b)])
print(c)
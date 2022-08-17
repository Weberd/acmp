p, s = input().split()
p = int(p)

if p > 0:
    print(s[:p-1] + s[p:])
else:
    print(s[1:])
r1, r2, r3 = map(int, input().split())

if 2 * r2 + 2 * r3 <= 2 * r1:
    print('YES')
else:
    print('NO')
w, h, r = map(int, input().split())

if w >= r * 2 and h >= r * 2:
  print('YES')
else:
  print('NO')
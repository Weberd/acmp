import math
a = int(input())
if a > 0:
  print('YES') if math.log2(a) - int(math.log2(a)) == 0 else print('NO')
else:
  print('NO')
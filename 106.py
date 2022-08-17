n = int(input())
ones = zeroes = 0
for m in range(n):
    c = int(input())
    if c == 1:
        ones += 1
    else:
        zeroes += 1
if ones >= zeroes:
    print(ones + zeroes - ones)
else:
    print(ones + zeroes - zeroes)
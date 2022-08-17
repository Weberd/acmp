a, b, c = map(int, input().split())
m = max(a,b,c)

if a >= 94 and b >= 94 and c >= 94 and a <= 727 and b <= 727 and c <= 727:
    print(m)
else:
    print('Error')

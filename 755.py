x, y, z = map(int, input().split())
print(x + y - z) if x + y >= z else print('Impossible')
a = int(input())

# GCV
# GVC
# VGC

b = ['G', 'C', 'V']

for i in range(a):
    left = b[0]
    central = b[1]
    right = b[2]

    b[0] = right
    b[1] = left
    b[2] = central

print(''.join(b))
troom, tcond = map(int, input().split())
mode = input()

if mode == 'freeze':
    print(min(troom, tcond))

if mode == 'heat':
    print(max(troom, tcond))

if mode == 'auto':
    print(tcond)

if mode == 'fan':
    print(troom)
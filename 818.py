n = input()
a = list(map(int, input().split()))

print(sum(a) - (len(a)  - 1))
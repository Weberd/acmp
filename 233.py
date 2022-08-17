n = int(input())
bridges = map(int, input().split())

for i, bridge in enumerate(list(bridges)):
    if bridge <= 437:
        print("Crash", i + 1)
        exit(0)

print("No crash")
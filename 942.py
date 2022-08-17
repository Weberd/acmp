n = input()
c5 = list(map(int, input().split()))
time5 = 0
for i in range(len(c5) + 1):
    if i > 0:
        time5 += sum(c5[:i])

c3 = c5.copy()
c3.reverse()
time3 = 0
for i in range(len(c3) + 1):
    if i > 0:
        time3 += sum(c3[:i])

c1 = c5.copy()
c1.sort()
time1 = 0
for i in range(len(c1) + 1):
    if i > 0:
        time1 += sum(c1[:i])

time = min(time5, time3, time1)
n = []

if time == time5: n.append(5)
if time == time3: n.append(3)
if time == time1: n.append(1)

print(min(n))
dh, dm = map(int, input().split(':'))
h, m = map(int, input().split())

ah = dh + h
am = dm + m

if dm + m > 59:
    ah += am // 60

ah %= 24
am %= 60

print("{:0>2d}:{:0>2d}".format(ah, am))
y = int(input())

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("12/09/{:0>4d}".format(y))
else:
    print("13/09/{:0>4d}".format(y))

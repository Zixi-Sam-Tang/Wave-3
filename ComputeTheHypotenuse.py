import math
def hypot(leg1, leg2):
    return math.sqrt(leg1 ** 2 + leg2 ** 2)
leg1 = int(input("Input the first leg: "))
leg2 = int(input("Input the second leg: "))
print("{:.2f}".format(hypot(leg1, leg2)))
def calculate(num):
    return 10.95 + 2.95 * (num - 1)
num = int(input("How many items?: "))
print("{:.2f}".format(calculate(num)))
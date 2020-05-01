import math
num = int(input("Enter an integer (2 or greater): "))
while num < 2:
    num = int(input("Invaild input please input again: "))
print("The prime factors of " + str(num) + " are:")
numprime = True
for i in range(2, int(math.floor(num//2)) + 1):
    prime = True
    for j in range(2, int(math.floor(i//2)) + 1):
        if i % j == 0:
            prime = False
    while num % i == 0 and prime:
        print(i)
        num = num / i
        numprime = False
if numprime:
    print(num)
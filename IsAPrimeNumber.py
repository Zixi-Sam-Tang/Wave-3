def isPrime():
    num = int(input("Input a number: "))
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            return False
    return True
if isPrime(): print("Is prime")
else: print("Not prime")
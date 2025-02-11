def func(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

n = int(input("Enter a number: "))
print(func(n))
def func(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

n = int(input("Enter a number: "))
print(func(n))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

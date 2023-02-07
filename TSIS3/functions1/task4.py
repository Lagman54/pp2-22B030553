def isPrime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def filter_prime(arr):
    primes = []
    for el in arr:
        if isPrime(el):
            primes.append(el)
    return primes


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(filter_prime(a))

def isPrime(x):
    if x == 0 or x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
arr = [int(i) for i in range(n + 1)]

primes = filter(isPrime, arr)
print(*primes)

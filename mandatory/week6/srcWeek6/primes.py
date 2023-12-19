import random

def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1:
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result

def WITNESS(a, d, n, s):
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return False

    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False

    return True

def miller_rabin(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        if WITNESS(a, d, n, s):
            return False

    return True



def test_miller_rabin_large_primes():
    primes_to_test = [99999959, 99999941, 99999931, 99999989, 99999971]  # Add more primes as needed
    k = 20  # Number of iterations for the Miller-Rabin test

    for prime in primes_to_test:
        if miller_rabin(prime, k):
            print(f"{prime} is probably a prime.")
        else:
            print(f"{prime} is not a prime.")

if __name__ == "__main__":
    test_miller_rabin_large_primes()

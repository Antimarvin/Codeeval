__author__ = 'Richard L. Sweat Jr.'


def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i


def get_primes(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1


def main():
    total = 0
    for i in get_primes(1000):
        total += i
    return total


if __name__ == '__main__':
    print main()

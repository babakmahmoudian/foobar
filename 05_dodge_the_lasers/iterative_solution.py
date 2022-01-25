sqrt2_minus1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


def solution(s):
    s = int(s)

    n_primes = {}
    n = s
    while True:
        n_prime = int(sqrt2_minus1 * n / 10**100)
        n_primes[n_prime] = n
        n = n_prime
        if n_prime == 0:
            break

    n_prime = 0
    res = 0
    while n < s:
        n = n_primes[n_prime]
        res = n * n_prime + n * (n + 1) // 2 - n_prime * (n_prime + 1) // 2 - res
        n_prime = n

    return str(res)

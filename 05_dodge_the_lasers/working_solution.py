# str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.
# https://oeis.org/search?q=floor%28n*sqrt%282%29%29&sort=&language=&go=Search
# sqrt(2) upto 100 decimal '1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727'
# http://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

minus_sqrt2 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


def n1(n):
    return (minus_sqrt2 * n) // (10**100)


def s(n):
    if n == 1:
        return 1

    if n < 1:
        return 0
    return n * n1(n) + n * (n + 1) / 2 - n1(n) * (n1(n) + 1) / 2 - s(n1(n))


def solution(n):
    n = long(n)
    return str(s(n))

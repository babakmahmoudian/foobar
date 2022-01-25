sqrt2_minus1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


def solution(s):
    def calc_seq(n):
        n_prime = int(sqrt2_minus1 * n / 10**100)

        if n == 1:
            return 1

        if n < 1:
            return 0

        val = n * n_prime + n * (n + 1) // 2 - n_prime * (n_prime + 1) // 2
        return val - int(solution(n_prime))

    return str(calc_seq(int(s)))

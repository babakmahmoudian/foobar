def solution(s):
    s = int(s)
    sums = 0
    while s > 0:
        sums += int(s * pow(2, .5))
        s -= 1
    return str(sums)

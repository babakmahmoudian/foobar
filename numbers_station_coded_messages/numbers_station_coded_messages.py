def solution_1(l, t):
    for i in range(len(l)):
        if l[i] > t:
            continue
        sum = 0
        for j in range(i, len(l)):
            sum += l[j]
            if sum == t:
                return [i, j]
            if sum > t:
                break
    return [-1, 1]

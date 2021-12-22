def solution_1(l, t):
    for i in range(len(l)):
        sum = 0
        for j in range(i, len(l)):
            sum += l[j]
            if sum == t:
                return [i, j]
            if sum > t:
                break
    return [-1, -1]


def solution_2(l, t):
    total_sum = 0
    start_index = 0

    for i in range(len(l)):
        total_sum += l[i]

        while total_sum > t:
            total_sum -= l[start_index]
            start_index += 1

        if total_sum == t:
            return [start_index, i]

    return [-1, -1]


def solution_3(l, t):
    prefix_sums = {0: -1}
    current_sum = 0
    for i in range(len(l)):
        current_sum += l[i]
        prefix_sums[current_sum] = i

        diff = current_sum - t
        if diff in prefix_sums:
            return [prefix_sums[diff] + 1, i]

    return [-1, -1]

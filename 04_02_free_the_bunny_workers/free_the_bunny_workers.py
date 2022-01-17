def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution(num_buns, num_required):
    def add_keys(idx_list, start_index, depth, remaining_keys):
        if depth == 0:
            key = remaining_keys.pop(-1)
            for i in range(len(dist)):
                if i not in idx_list:
                    dist[i].insert(0, key)
            return

        depth -= 1
        for i in range(start_index, len(dist)):
            add_keys(idx_list[:] + [i], i + 1, depth, remaining_keys)

    key_count = combination(num_buns, num_required - 1)

    dist = [[] for i in range(num_buns)]
    add_keys([], 0, num_required - 1, range(key_count))

    return dist


def print_solution(sol):
    print(''.join(['[\n'] + ['  %s,\n' % s for s in sol] + [']']))


solution(3, 1)
# # [
# #   [0],
# #   [0],
# #   [0],
# # ]

solution(4, 4)
# # [
# #   [0],
# #   [1],
# #   [2],
# #   [3],
# # ]

solution(3, 2)
# # [
# #   [0, 1],
# #   [0, 2],
# #   [1, 2],
# # ]


solution(5, 3)
# [
#   [0, 1, 2, 3, 4, 5],
#   [0, 1, 2, 6, 7, 8],
#   [0, 3, 4, 6, 7, 9],
#   [1, 3, 5, 6, 8, 9],
#   [2, 4, 5, 7, 8, 9],
# ]

solution(4, 2)
# # [
# #   [0, 1, 2],
# #   [0, 1, 3],
# #   [0, 2, 3],
# #   [1, 2, 3],
# # ]

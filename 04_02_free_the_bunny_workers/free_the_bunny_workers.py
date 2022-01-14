def solution(num_buns, num_required):
    pass


def print_solution(num_buns, num_required):
    sol = solution(num_buns, num_required)
    print(''.join(['[\n'] + ['  %s,\n' % s for s in sol] + [']']))


print_solution(3, 1)
# 0
# 1

print_solution(2, 2)
# 0, 1

print_solution(3, 2)

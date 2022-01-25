from recursive_solution import solution as r_solution
from iterative_solution import solution as i_solution
from working_solution import solution as w_solution


start_range = pow(10, 90) + 1

for i in range(start_range, start_range + 100):
    rsol = r_solution(i)
    isol = i_solution(i)
    wsol = w_solution(i)

    if rsol != wsol or isol != wsol:
        print('-' * 80)
        print("Error: s = %i =>\nrecursive = %s\niterative = %s\ncorrect =   %s" % (i, rsol, isol, wsol))

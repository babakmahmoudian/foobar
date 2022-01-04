from ion_flux_relabeling import solution_1, solution_2
from random import randrange, sample
import time


def run():
    compare()


def compare():
    t1 = 0
    t2 = 0
    for i in range(0, 10000):
        h = randrange(7, 31)
        q = sample(range(1, pow(2, h)), randrange(1, 100))

        start = time.time()
        result1 = solution_1(h, q)
        end = time.time()
        t1 += (end - start)

        start = time.time()
        result2 = solution_2(h, q)
        end = time.time()
        t2 += (end - start)

        if result1 != result2:
            print("solution_1 != solution_2: (h = %d, q = %s) => [%s] != [%s]" % (
                h, q, result1, result2))

    print("total time solution_1: {}".format(t1))
    print("total time solution_2: {}".format(t2))


if __name__ == '__main__':
    run()

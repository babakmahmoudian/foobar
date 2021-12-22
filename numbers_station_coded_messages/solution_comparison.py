from numbers_station_coded_messages import solution_1, solution_2, solution_3
from random import randrange
import time


def run():
    test()


def test():
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(0, 1000000):
        l = random_list()
        t = randrange(10, 30)

        start = time.process_time()
        i1, j1 = solution_1(l, t)
        end = time.process_time()
        t1 += (end - start)

        start = time.process_time()
        i2, j2 = solution_2(l, t)
        end = time.process_time()
        t2 += (end - start)

        start = time.process_time()
        i3, j3 = solution_3(l, t)
        end = time.process_time()
        t3 += (end - start)

        if (i1 != i2 or j1 != j2):
            print("solution_2 failed: {}, {} => [{}, {}] != [{}, {}]".format(
                l, t, i1, j1, i2, j2))

        if (i1 != i3 or j1 != j3):
            print("solution_3 failed: {}, {} => [{}, {}] != [{}, {}]".format(
                l, t, i1, j1, i3, j3))

    print("total time solution_1: {}".format(t1))
    print("total time solution_2: {}".format(t2))
    print("total time solution_3: {}".format(t3))


def random_list():
    l = []
    for i in range(0, 10):
        l.append(randrange(1, 10))
    return l


if __name__ == '__main__':
    run()

import skipping_work
import random
import time
from tabulate import tabulate
import sys
import inspect

sample_config = {
    "default": {
        "sample_count": 20000,
        "sample_length": 99,
    },
    "lengthy": {
        "sample_count": 2000,
        "sample_length": 500,
    },
    "short": {
        "sample_count": 50000,
        "sample_length": 5,
    },
}


def create_samples(count, length):
    def create_single_sample(common_nums, extra_num):
        x = list(common_nums)
        y = x[:]
        random.shuffle(y)
        y.insert(random.randint(0, len(x) - 1), extra_num)
        return x, y

    samples = []
    for i in range(count):
        common_nums = list(random.sample(
            range(-1000, 1000), length))
        extra_num_index = random.randint(0, len(common_nums) - 1)
        extra_num = common_nums.pop(extra_num_index)
        samples.append(create_single_sample(common_nums, extra_num))

    return samples


def calc_solution_time(solution, samples):
    starting_time = time.process_time()

    for sample in samples:
        _ = solution(sample[0], sample[1])

    elapsed_time = time.process_time() - starting_time

    return elapsed_time


if __name__ == '__main__':
    solution_names = [solution_name for solution_name, solution in inspect.getmembers(
        skipping_work, inspect.isfunction)]

    for key, value in sample_config.items():
        sample_count = sample_config[key]["sample_count"]
        sample_length = sample_config[key]["sample_length"]

        sys.stdout.write("Using %s sample data: Count=%d Length=%d\n\n" %
                         (key, sample_count, sample_length))

        samples = create_samples(count=sample_count, length=sample_length)

        solution_times = []
        for _, solution in inspect.getmembers(skipping_work, inspect.isfunction):
            solution_times.append(
                [solution.__doc__, calc_solution_time(solution, samples)]
            )

        sys.stdout.write(
            tabulate(solution_times, headers=['solution', 'time']))
        sys.stdout.write('\n\n')

    sys.stdout.write(
        "Gradually incrementing the length of input data\n\n")
    solution_times = []
    for count in range(50, 1001, 50):
        samples = create_samples(5000, count)
        current_times = [str(count)]
        for solution_name in solution_names:
            solution = getattr(skipping_work, solution_name)
            current_times.append(
                str(calc_solution_time(solution, samples))
            )
        solution_times.append(current_times)

    for i in range(len(solution_times) - 1, 0, -1):
        for j in range(len(solution_names), 0, -1):
            st = float(solution_times[i][j])
            pre_st = float(solution_times[i-1][j])
            first_st = float(solution_times[0][j])
            mul = st/pre_st if pre_st else 0
            mul_total = st/first_st if first_st else 0
            solution_times[i][j] += " -> *%.1f (*%.1f)" % (mul, mul_total)

    sys.stdout.write(
        tabulate(solution_times, headers=['count'] + solution_names))
    sys.stdout.write('\n\n')

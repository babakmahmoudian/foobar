import skipping_work
import random
import time
from tabulate import tabulate

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
    for key, value in sample_config.items():
        sample_count = sample_config[key]["sample_count"]
        sample_length = sample_config[key]["sample_length"]

        print("Using %s sample data: Count=%d Length=%d" %
              (key, sample_count, sample_length))

        print("Creating samples...", end=' ', flush=True)

        samples = create_samples(count=sample_count, length=sample_length)

        print("Done!", flush=True)

        solution_times = []
        print("Calculating process times:")
        for i in range(1, 5):
            solution = getattr(skipping_work, "solution_%d" % i)

            print("Calculating for %s..." %
                  solution.__doc__, end=' ', flush=True)

            solution_times.append(
                [solution.__doc__, calc_solution_time(solution, samples)]
            )

            print("Done!", flush=True)

        print('\n')
        print(tabulate(solution_times, headers=['solution', 'time']))
        print('\n')

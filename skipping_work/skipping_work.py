from array import array


def solution_1(x, y):
    '''Solution 1: Union + (not in)'''

    union = x + y
    for id in union:
        if id not in x or id not in y:
            return id


def solution_2(x, y):
    '''Solution 2: Sort and compare'''

    x.sort()
    y.sort()
    for i in range(min(len(x), len(y))):
        x_id = x[i]
        y_id = y[i]
        if x_id != y_id:
            return min(x_id, y_id)
    return x[-1] if len(x) > len(y) else y[-1]


def solution_3(x, y):
    '''Solution 3: Convert to set and XOR'''

    return (set(x) ^ set(y)).pop()


def solution_4(x, y):
    '''Solution 4: Using dictionary (keys taken from x)'''

    all_ids = dict()

    for x_id in x:
        all_ids[x_id] = 1

    for y_id in y:
        try:
            all_ids[y_id] += 1
        except KeyError:
            return y_id

    for key, value in all_ids.items():
        if value == 1:
            return key


def solution_5(x, y):
    '''Solution 5: Using list of 2000'''

    all_ids = [0 for _ in range(2000)]

    for id in x:
        all_ids[id + 1000] += 1

    for id in y:
        all_ids[id + 1000] += 1

    for i in range(2000):
        if all_ids[i] == 1:
            return i - 1000


def solution_6(x, y):
    '''Solution 6: Using array of 2000'''

    all_ids = array('H', [0 for _ in range(2000)])

    for id in x:
        all_ids[id + 1000] += 1

    for id in y:
        all_ids[id + 1000] += 1

    for i in range(2000):
        if all_ids[i] == 1:
            return i - 1000

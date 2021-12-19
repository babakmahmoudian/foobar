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
        if x[i] != y[i]:
            return min(x[i], y[i])
    return x[-1] if len(x) > len(y) else y[-1]


def solution_3(x, y):
    '''Solution 3: Convert to set and XOR'''

    return (set(x) ^ set(y)).pop()


def solution_4(x, y):
    '''Solution 4: Using dictionary with keys form -1000 to 1000'''

    all_ids = dict.fromkeys(range(-1000, 1000), 0)

    for x_id in x:
        all_ids[x_id] = 1

    for y_id in y:
        all_ids[y_id] += 1

    for key, value in all_ids.items():
        if value == 1:
            return key

# *********************************************
# Solution 1: Union + (not in)
# *********************************************
# def solution(x, y):
#     union = x + y
#     for id in union:
#         if id not in x or id not in y:
#             return id

# *********************************************
# Solution 2: Sort and difference
# *********************************************
def solution(x, y):
    x.sort()
    y.sort()
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            return min(x[i], y[i])
    return x[-1] if len(x) > len(y) else y[-1]

# *********************************************
# Solution 3: Convert to set and XOR
# *********************************************
# def solution(x, y):
#     return (set(x) ^ set(y)).pop()

# *********************************************
# Test Cases
# *********************************************


def test_x_has_extra():
    x = [13, 5, 6, 2, 5]    # -> [2, 5, 5, 6, 13]
    y = [5, 2, 5, 13]       # -> ]2, 5, 5, 13]
    expected = 6

    actual = solution(x, y)

    assert actual == expected


def test_y_has_extra():
    # x = [1, 1, 2, 3, 4, 14, 27, 50]
    # y = [-4, 1, 1, 2, 3, 4, 14, 27, 50]
    x = [14, 27, 1, 4, 2, 50, 3, 1]
    y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
    expected = -4

    actual = solution(x, y)

    assert actual == expected


def test_x_has_extra_at_beginning():
    x = [-1, 1, 2, 3, 4]
    y = [1, 2, 3, 4]
    expected = -1

    actual = solution(x, y)

    assert actual == expected


def test_y_has_extra_at_beginning():
    x = [1, 2, 3, 4]
    y = [-1, 1, 2, 3, 4]
    expected = -1

    actual = solution(x, y)

    assert actual == expected


def test_x_has_extra_at_end():
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4]
    expected = 5

    actual = solution(x, y)

    assert actual == expected


def test_y_has_extra_at_end():
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4, 5]
    expected = 5

    actual = solution(x, y)

    assert actual == expected


def test_x_is_empty():
    x = []
    y = [1]
    expected = 1

    actual = solution(x, y)

    assert actual == expected


def test_y_is_empty():
    x = [1]
    y = []
    expected = 1

    actual = solution(x, y)

    assert actual == expected

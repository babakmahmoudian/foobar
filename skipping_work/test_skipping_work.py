from skipping_work import solution_4 as solution


def test_x_has_extra():
    x = [13, 5, 6, 2, 5]    # -> [2, 5, 5, 6, 13]
    y = [5, 2, 5, 13]       # -> [2, 5, 5, 13]
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


# def test_x_has_extra_duplicate():
#     x = [1, 2, 2, 3, 4]
#     y = [1, 2, 3, 4]
#     expected = 2

#     actual = solution(x, y)

#     assert actual == expected


# def test_y_has_extra_duplicate():
#     x = [1, 2, 3, 4]
#     y = [1, 2, 2, 3, 4]
#     expected = 2

#     actual = solution(x, y)

#     assert actual == expected

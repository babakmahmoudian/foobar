from numbers_station_coded_messages import solution_3 as solution


def test_find_seq():
    l = [4, 3, 10, 2, 8]
    t = 12
    expected = [2, 3]

    actual = solution(l, t)

    assert actual == expected


def test_find_seq_more_than_one_seq():
    l = [4, 3, 5, 7, 8]
    t = 12
    expected = [0, 2]

    actual = solution(l, t)

    assert actual == expected


def test_find_seq_first_element_equal_to_sum():
    l = [12, 3, 10, 2, 8]
    t = 12
    expected = [0, 0]

    actual = solution(l, t)

    assert actual == expected


def test_find_seq_first_element_greater_than_sum():
    l = [17, 3, 10, 2, 8]
    t = 12
    expected = [2, 3]

    actual = solution(l, t)

    assert actual == expected


def test_find_seq_middle_element_greater_than_sum():
    l = [1, 17, 10, 2, 8]
    t = 12
    expected = [2, 3]

    actual = solution(l, t)

    assert actual == expected


def test_find_seq_ignoring_first_element():
    l = [1, 2, 3, 4, 5]
    t = 9
    expected = [1, 3]

    actual = solution(l, t)

    assert actual == expected


def test_not_find_seq():
    l = [1, 2, 3, 4]
    t = 15
    expected = [-1, -1]

    actual = solution(l, t)

    assert actual == expected

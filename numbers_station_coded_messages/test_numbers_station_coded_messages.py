from numbers_station_coded_messages import solution_1 as solution


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


def test_not_find_seq():
    l = [1, 2, 3, 4]
    t = 15
    expected = [-1, 1]

    actual = solution(l, t)

    assert actual == expected

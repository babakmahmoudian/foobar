from doomsday_fuel import solution_1 as solution


def test_given_test_case_1():
    m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    expected = [7, 6, 8, 21]

    actual = solution(m)

    assert actual == expected


def test_given_test_case_2():
    m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    expected = [0, 3, 2, 9, 14]

    actual = solution(m)

    assert actual == expected

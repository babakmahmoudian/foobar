from iterative_solution import solution


def test_given_case_1():
    s = '77'
    expected = '4208'

    actual = solution(s)

    assert actual == expected


def test_given_case_2():
    s = '5'
    expected = '19'

    actual = solution(s)

    assert actual == expected

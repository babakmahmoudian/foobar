from fuel_injection_perfection import solution


def test_given_case_1():
    n = '15'
    expected = 5

    actual = solution(n)

    assert actual == expected


def test_given_case_2():
    n = '4'
    expected = 2

    actual = solution(n)

    assert actual == expected

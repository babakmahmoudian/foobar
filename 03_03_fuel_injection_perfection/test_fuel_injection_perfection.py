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


def test_one():
    n = '1'
    expected = 0

    actual = solution(n)

    assert actual == expected


def test_two():
    n = '2'
    expected = 1

    actual = solution(n)

    assert actual == expected


def test_three():
    n = '3'
    expected = 2

    actual = solution(n)

    assert actual == expected


def test_big_number():
    n = '12412124512857890124132412452319283712549081240098123409125132059812349021'
    expected = 327

    actual = solution(n)

    assert actual == expected

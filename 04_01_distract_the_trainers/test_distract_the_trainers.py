from distract_the_trainers import solution


def test_given_case_1():
    banana_list = [1, 1]
    expected = 2

    actual = solution(banana_list)

    assert actual == expected


def test_given_case_2():
    banana_list = [1, 7, 3, 21, 13, 19]
    expected = 0

    actual = solution(banana_list)

    assert actual == expected

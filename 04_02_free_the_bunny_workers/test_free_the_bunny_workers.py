from free_the_bunny_workers import solution


def test_given_case_1():
    num_buns = 2
    num_required = 1
    expected = [[0], [0]]

    actual = solution(num_buns, num_required)

    assert actual == expected


def test_given_case_2():
    num_buns = 4
    num_required = 4
    expected = [[0], [1], [2], [3]]

    actual = solution(num_buns, num_required)

    assert actual == expected


def test_given_case_3():
    num_buns = 3
    num_required = 2
    expected = [[0, 1],
                [0, 2],
                [1, 2],
                ]

    actual = solution(num_buns, num_required)

    assert actual == expected


def test_given_case_4():
    num_buns = 5
    num_required = 3
    expected = [[0, 1, 2, 3, 4, 5],
                [0, 1, 2, 6, 7, 8],
                [0, 3, 4, 6, 7, 9],
                [1, 3, 5, 6, 8, 9],
                [2, 4, 5, 7, 8, 9]
                ]

    actual = solution(num_buns, num_required)

    assert actual == expected

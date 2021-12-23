from ion_flux_relabeling import solution_1 as solution


def test_find_parents_including_root():
    h = 3
    q = [7, 3, 5, 1]
    expected = [-1, 7, 6, 3]

    actual = solution(h, q)

    assert actual == expected


def test_find_parents_not_including_root():
    h = 5
    q = [19, 14, 28]
    expected = [21, 15, 29]

    actual = solution(h, q)

    assert actual == expected


def test_find_parent_of_child_of_root():
    h = 5
    q = [30]
    expected = [31]

    actual = solution(h, q)

    assert actual == expected


def test_find_parent_of_root():
    h = 5
    q = [31]
    expected = [-1]

    actual = solution(h, q)

    assert actual == expected

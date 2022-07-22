from disorderly_escape import solution


def test_1():
    w = 2
    h = 3
    s = 4
    expected = 430

    actual = solution(w, h, s)

    assert actual == expected


def test_2():
    w = 2
    h = 2
    s = 2
    expected = 7

    actual = solution(w, h, s)

    assert actual == expected

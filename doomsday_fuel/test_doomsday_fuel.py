from doomsday_fuel_1 import solution as my_solution
from working_solution import solution as working_solution


def test_given_test_case_1():
    m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected


def test_given_test_case_2():
    m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected


def test_absorbing_state_in_middle():
    m = [[0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected


def test_one_state():
    m = [[0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected


def test_two_states():
    m = [[0, 3], [0, 0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected


def all_states_absorbing():
    m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    expected = working_solution(m)

    actual = my_solution(m)

    assert actual == expected

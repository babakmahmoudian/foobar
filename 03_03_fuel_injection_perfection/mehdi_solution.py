map = {}
MAX = 200


def init():
    map[1] = (0, (1, ))
    follow(1)


def follow(number):
    update(number, number + 1)
    update(number, number - 1)
    update(number, number * 2)


def update(origin, new_number):
    if new_number < 1 or new_number > MAX:
        return
    distance0, path0 = map[origin]
    if new_number not in map or map[new_number][0] > distance0 + 1:
        map[new_number] = (distance0 + 1, path0 + (origin,))
        if new_number <= 99:
            follow(new_number)


def solution(number, log=False):
    init()
    if log:
        return map[number][1][1:]
    return map[number][0]

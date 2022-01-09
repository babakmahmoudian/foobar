def solution(n):
    number = int(n)
    total_op = 0

    while number > 1:
        if number == 3:
            number -= 1
            total_op += 1

        if number % 2 == 0:
            number = number // 2
        elif (number + 1) % 4 == 0:
            number += 1
        else:
            number -= 1
        total_op += 1

    return total_op

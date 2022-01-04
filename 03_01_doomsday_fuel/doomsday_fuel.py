from fractions import Fraction
from functools import reduce


def solution(m):
    if len(m) < 2:
        return [1, 1]

    (std_form_r, std_form_f) = get_std_form_parts(m)

    f_cross_r = multiply_matrix(std_form_f, std_form_r)

    preliminary_result = f_cross_r[0]
    lcm = get_lcm(preliminary_result)
    return [int(x.numerator * (lcm / x.denominator)) for x in preliminary_result] + [lcm]


def get_std_form_parts(matrix):
    absorbing_states = []
    non_absorbing_states = []
    for i in range(len(matrix)):
        if all(x == 0 for x in matrix[i]):
            absorbing_states.append(i)
        else:
            non_absorbing_states.append(i)

    std_form_r = []
    std_form_q = []

    for i in non_absorbing_states:
        sum_of_row = sum(matrix[i])
        row = []
        for j in absorbing_states:
            row.append(Fraction(matrix[i][j], sum_of_row))
        for j in non_absorbing_states:
            row.append(Fraction(matrix[i][j], sum_of_row))

        std_form_r.append(row[:len(absorbing_states)])
        std_form_q.append(row[len(absorbing_states):])

    tmp_std_form_f = []
    for i in range(len(non_absorbing_states)):
        row = []
        for j in range(len(non_absorbing_states)):
            current_element = std_form_q[i][j]
            row.append((Fraction(1) if i == j else Fraction(0)) -
                       current_element)
        tmp_std_form_f.append(row)
    std_form_f = get_invert_matrix(tmp_std_form_f)

    return (std_form_r, std_form_f)


def get_invert_matrix(matrix):
    def get_minor(matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    def transpose(matrix):
        return map(list, zip(*matrix))

    def get_deternminant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = Fraction(0)
        for c in range(len(matrix)):
            determinant += Fraction((-1)**c) * \
                matrix[0][c] * get_deternminant(get_minor(matrix, 0, c))
        return determinant

    if len(matrix) == 1:
        return [[Fraction(1) / matrix[0][0]]]

    determinant = get_deternminant(matrix)

    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
                [-matrix[1][0] / determinant, matrix[0][0] / determinant]]

    cofactors = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            minor = get_minor(matrix, i, j)
            new_element = Fraction((-1)**(i + j)) * get_deternminant(minor)
            row.append(new_element)
        cofactors.append(row)
    cofactors = list(transpose(cofactors))
    for i in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[i][j] = cofactors[i][j] / determinant

    return cofactors


def multiply_matrix(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix2[0])):
            s = Fraction(0)
            for k in range(0, len(matrix1[0])):
                s += matrix1[i][k] * matrix2[k][j]
            temp.append(s)
        result.append(temp)

    return result


def get_lcm(fractions):
    def calc_lcm(a, b):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return a * b // gcd(a, b)

    denominators = [x.denominator for x in fractions]
    return reduce(calc_lcm, denominators)

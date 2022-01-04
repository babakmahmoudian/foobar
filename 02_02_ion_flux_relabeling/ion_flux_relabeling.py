def solution_1(h, q):
    def get_parent_index(h, child):
        if child == pow(2, h) - 1:
            return -1

        acc = 0
        pre_child = child
        while ((child + 1) & (child) != 0) and ((child + 2) & (child + 1) != 0):
            child -= pow(2, len(bin(child)) - 3) - 1
        acc = pre_child - child

        if (child + 1) & (child) == 0:
            child = child * 2 + 1
        elif (child + 2) & (child + 1) == 0:
            child += 1

        return child + acc

    return [get_parent_index(h, node_index) for node_index in q]


def solution_2(h, q):
    def get_parent_index(h, child):
        root = pow(2, h) - 1

        if child == root:
            return -1

        leftmost = parent = root
        while leftmost > 0:
            left_child = parent - (leftmost + 1) // 2
            right_child = parent - 1

            if (child == left_child) or (child == right_child):
                return parent

            parent = left_child if child < left_child else right_child
            leftmost = (leftmost - 1) // 2

    return [get_parent_index(h, node_index) for node_index in q]


def get_id(index):
    def generate_id_pool():
        def is_prime(num):
            return False if num < 2 else all(num % i != 0 for i in range(2, int(num**0.5) + 1))

        next_prime = 2
        id_pool = ""
        while len(id_pool) < 10004:
            if is_prime(next_prime):
                id_pool += str(next_prime)
            next_prime += 1
        return id_pool

    id_pool = generate_id_pool()
    return id_pool[index:index+4]


# ********** Test Cases **********

def test_index_0():
    index = 0

    id = get_id(index)

    assert "2357" == id


def test_index_10000():
    index = 10000

    id = get_id(index)

    assert "0219" == id

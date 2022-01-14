def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def get_loops(banana_list):
    def can_loop(x, y):
        xy = (x + y) // gcd(x, y)
        return xy & (xy - 1)

    length = len(banana_list)
    loops = {i: set() for i in range(length)}
    for i in range(length):
        for j in range(i + 1, length):
            x = banana_list[i]
            y = banana_list[j]
            if can_loop(x, y):
                loops[i].add(j)
                loops[j].add(i)
    return loops


def get_paired_count(loops):
    def dfs(src, pairings, visited):
        for dest in range(length):
            if dest in loops[src] and not visited[dest]:
                visited[dest] = True
                if pairings[dest] == -1 or dfs(pairings[dest], pairings, visited):
                    pairings[dest] = src
                    return True
        return False

    length = len(loops)
    pairings = [-1] * length
    total = 0
    for i in range(length):
        visited = [False] * length
        if dfs(i, pairings, visited):
            total += 1
    return total >> 1 << 1


def solution(banana_list):
    loops = get_loops(banana_list)
    paired_count = get_paired_count(loops)
    return(len(banana_list) - paired_count)

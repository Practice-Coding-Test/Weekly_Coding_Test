from itertools import combinations

def solution(enter, leave):
    N = len(enter)
    answer = [set() for i in range(N+1)]
    for out in leave:
        tmp = []
        for i, v in enumerate(enter):
            if v != -1:
                tmp.append(v)
            if v == out:
                enter[i] = -1
                break
        for v, u in combinations(tmp, 2):
            answer[v].add(u)
            answer[u].add(v)

    return [len(s) for s in answer[1:]]
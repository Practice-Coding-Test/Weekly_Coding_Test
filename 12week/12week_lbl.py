from itertools import permutations
def solution(k, dungeons):
    MAX = 0
    for permut in permutations(dungeons):
        now_k = k
        cnt = 0
        for idxå in range(len(dungeons)):
            if now_k < permut[idx][0]:
                continue
            now_k -= permut[idx][1]
            cnt += 1
        MAX = max(MAX, cnt)
    return MAX

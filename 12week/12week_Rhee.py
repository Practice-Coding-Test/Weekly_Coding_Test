def solution(k, dungeons):
    from itertools import permutations
    cnts = []
    for i in permutations(dungeons):
        cnt = 0; kk = k
        for j in range(len(dungeons)):
            if i[j][0] <= kk:
                kk -= i[j][1]; cnt += 1
        cnts.append(cnt)
    return max(cnts)

def solution(k, dungeons):
    import itertools

    result = list(itertools.permutations(dungeons, len(dungeons)))

    ans = 0
    for seqes in result:
        tmp_k = k
        for i in range(len(dungeons)):
            if tmp_k >= seqes[i][0]:
                tmp_k -= seqes[i][1]
            else:
                i -= 1
                break
        tmp = i + 1
        ans = max(ans, tmp)

    return ans

import itertools
def solution(k, dungeons):
    result = []
    dungeon = itertools.permutations(dungeons, len(dungeons))
    for dun in dungeon:
        answer = 0
        hp = k
        for d in dun:
            if hp >= d[0]:
                hp -= d[1]
                answer += 1
            else:
                break
        result.append(answer)
    return max(result)
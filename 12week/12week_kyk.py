from itertools import permutations
def solution(k, dungeons):
    n,answer= len(dungeons),0
    item = [i for i in range(n)]
    items = list(permutations(item, n))

    for item in items:
        power, temp= k, 0
        for idx in item:
            dungeon= dungeons[idx]
            need, used = dungeon[0], dungeon[1]

            if need <= power:
                power -= used
                temp += 1
            else:
                break
            answer= max(answer,temp)
            if answer == n:
                return n

    return answer

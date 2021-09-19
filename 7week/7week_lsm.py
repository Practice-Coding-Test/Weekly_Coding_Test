def solution_7(enter, leave):
    result = [0] * len(enter)

    check = []

    idx = 0
    for i in leave:
        # 퇴실할 사람이 방에 들어올 때까지 입실
        while i not in check:
            check.append(enter[idx])
            idx += 1
        # 퇴실할 사람이 방에 들어온다면, 해당 사람 퇴실
        check.remove(i)

        # 현재 방에 있는 사람들이 만난 사람 수에 1씩 더해줌
        for j in check:
            result[j-1] += 1
        
        # 퇴실한 사람의 만난 사람 수에 현재 방 인원수를 더해줌
        result[i-1] += len(check)

    return result

print(solution_7([1,4,2,3], [2,1,3,4]))


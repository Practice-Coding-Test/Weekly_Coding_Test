def solution(enter, leave):
    idx = enter.index(leave[0])
    room = enter[:idx] # 가장 먼저 떠나는 사람이 나갈 때 회의실에 있는 사람
    answer = [1 if i in room else 0 for i in range(len(enter)+1)] # 첫번째 사람 나갈 때 room에 있던 사람 한 번씩 만난다.
    answer[leave[0]] = len(room) # 나가는 사람은 room에 있는 사람 수만큼 만난다.
    for l in leave[1:-1]:
        while not l in room: # 해당 room에 사람이 들어올때까지
            idx += 1
            room.append(enter[idx])
        room.remove(l)
        answer[l] += len(room)
        for r in room:
            answer[r] += 1
    return answer[1:]

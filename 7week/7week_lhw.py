from collections import deque

#https://j-ungry.tistory.com/189에서 deque 참고하였습니다


def solution(enter, leave):
    answer = [0] * (len(enter)+1)
    leave = deque(leave)

    room = []
    for entrance in enter:
        for rooms in room:
            answer[rooms] = answer[rooms] + 1
        answer[entrance] = answer[entrance] + len(room)
        room.append(entrance)

        while leave and leave[0] in room:
            room.remove(leave.popleft())
    answer = answer[1:]
    return answer

def solution(enter, leave):
    room = []
    meet = {}
    # by monitoring the room
    for e in enter:
        # to reduce time cose
        if enter[enter.index(e):] == leave[enter.index(e):]:
            for e in enter[enter.index(e):]:
                meet[e] = 0
            break
        room.append(e)
        # to find which person meet others in the room
        for k in room:
            if k in meet:
                meet[k] = meet[k] | set(room)
            else:
                meet[k] = set(room)
        # to make person leave from the room
        while leave[0] in room:
            room.remove(leave[0])
            # calculate how many people does each meet
            meet[leave[0]] = len(meet[leave[0]]) - 1
            leave = leave[1:]
            if len(leave) == 0:
                break
    # sort by order
    answer = list(dict(sorted(meet.items())).values())
    return answer

def solution(enter, leave):
    room = []
    meet = {}
    for e in enter:
        room.append(e)
        for k in room:
            if k in meet:
                meet[k] = meet[k] | set(room)
            else: meet[k] = set(room)
        while leave[0] in room:
            room.remove(leave[0])
            meet[leave[0]] = len(meet[leave[0]]) - 1
            leave = leave[1:]
            if len(leave)==0: break

    answer = list(dict(sorted(meet.items())).values())
    return answer
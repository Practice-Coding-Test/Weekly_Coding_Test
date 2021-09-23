
def solution(enter, leave): 
    answer= [0 for _ in range(len(enter)+1)]
    room= [] #회의실
  
    for go in enter:  #한명씩 들어가기        
        for already in room: #회의실에 있던 사람들이 현재 들어온 사람을 만나니까 1씩 더해줌
            answer[already] += 1

        answer[go] += len(room)  #현재 들어온 사람은 회의실에 있는 사람 수 만큼 만남
        room.append(go) #현재 들어온 사람을 회의실에 추가

        while leave and leave[0] in room: #나갈 사람이 회의실에 있으면 회의실에서 빼줌
            room.remove(leave[0]) 
            leave.remove(leave[0])

    return answer[1:]

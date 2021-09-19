# 코테는 첨이라 https://latte-is-horse.tistory.com/232 를 참고했습니다.
# 느낀점 : 스스로 푼다기 보다, 참고 사이트 보며 이해하는 정도로 진행

def solution(enter, leave):
    # enter : 회의실 입실 순서가 담긴 정수 배열
    # leave : 퇴실 순서가 담긴 정수 배열 
    # 투포인터로 접근
    answer = [[] for _ in range(len(enter)+1)] #사람 수보다 1 크게 설정
    room = []  # 특정 시간에 회의실에 존재하는 사람들 저장
    enter_po, leave_po = 0, 0 # enter_po : enter 가리키는 포인터
    
    while enter_po<len(enter) or leave_po<len(leave):
        if leave[leave_po] not in room:
            answer[enter[enter_po]]=room[:]
            room.append(enter[enter_po])
            enter_po += 1
        else:
            room.remove(leave[leave_po])
            leave_po += 1
    for p, person in enumerate(answer):
        for met in person:
            answer[met].append(p)
    return [len(set(i)) for i in answer][1:]

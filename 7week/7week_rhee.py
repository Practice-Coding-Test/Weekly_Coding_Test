def solution(enter, leave):
    answer = [[] for i in range(len(enter) +1)]
    tmp = []
    en_idx, le_idx = 0, 0

    while en_idx < len(enter):
        if leave[le_idx] not in tmp:
            # le_idx번째 사람이 나가기 전에 en_idx번쨰까지 들어온 사람 리스트 tmp를 answer에 추가
            answer[enter[en_idx]] = tmp[:]
            # 계속해서 en_idx를 늘려가면서 사람들을 tmp에 추가
            tmp.append(enter[en_idx])
            en_idx += 1
        else:
            # le_idx번째 사람이 나가면 방에서 나갔으니까 리스트에서 삭제
            tmp.remove(leave[le_idx])
            le_idx += 1

    for p, person in enumerate(answer):
        for met in person:
            # answer의 met번째 사람 자리에 만난 사람 리스트 추가
            answer[met].append(p)
    # 각 자리에 있는 리스트 길이를 재서 반환
    return [len(set(i)) for i in answer][1:]

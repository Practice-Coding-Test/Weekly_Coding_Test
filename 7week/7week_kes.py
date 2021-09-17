def solution(enter, leave):
    answer = [0 for i in range(len(enter))]
    out_idx = 0
    present = []

    for i in range(len(enter)):
        present.append(enter[i])

        if (len(present) > 1):  # 본인 이외 다른 원소들도 있는지
            for elem in present:
                if enter[i] == elem:  # 새로 들어온 원소인 경우 해당 자리에 본인 제외한 만난 개수 넣기
                    answer[elem - 1] = len(present) - 1
                else:
                    answer[elem - 1] += 1  # 이미 있으면 +1만 하기

        while leave[out_idx] in present:
            present.remove(leave[out_idx])  # 해당 원소 present에서 나오기
            if out_idx == len(enter) - 1:  # 마지막 인덱스면 반복문 탈출
                break
            out_idx += 1

    return answer

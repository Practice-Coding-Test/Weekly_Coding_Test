def solution(answers):
    p1 = [1,2,3,4,5] #수포자1
    p2 = [2,1,2,3,2,4,2,5] #수포자2
    p3 = [3,3,1,1,2,2,4,4,5,5] #수포자3
    score = [0,0,0]
    result = []
    
    for index, answer in enumerate(answers): # 각 학생 별 정답 개수
        print(index, answer)
        if answer == p1[index%len(p1)]:
            score[0] += 1
        if answer == p2[index%len(p2)]:
            score[1] += 1
        if answer == p3[index%len(p3)]:
            score[2] += 1
    
    for index, s in enumerate(score): # 가장 많은 개수의 학생
        if s == max(score):
            result.append(index+1)
            
    return result

def get_grade(number):
    if number >= 90:
        return 'A'
    elif 90 > number >= 80:
        return 'B'
    elif 80 > number >= 70:
        return 'C'
    elif 70 > number >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    student = []
    for i in range(len(scores)):
        sco = [score[i] for score in scores]
        if (sco.count(max(sco)) == 1 and sco[i] == max(sco)) or (sco.count(min(sco)) == 1 and sco[i] == min(sco)):
            sco.remove(sco[i])
        grade = sum(sco)/len(sco)
        answer += get_grade(grade)
    return answer
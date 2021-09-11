def solution(weights,head2head):
    answer = []
    for idx,(point,w) in enumerate(zip(head2head,weights)):
        ls = list(point)
        
        if ls.count('N') == len(ls): # 전적 0 일 때
            winner_rate = 0
        else:
            winner_rate = ls.count('W')/(ls.count('W')+ls.count('L')) # 승률 계산

        winner_idx = list(filter(lambda x: ls[x] == 'W', range(len(ls)))) # 승리한 사람의 번호
        over_weight_win = 0
        
        for i in winner_idx : 
            if weights[i] > w:
                over_weight_win += 1
                
        answer.append((-winner_rate,-over_weight_win,-w,idx+1)) # 조건부 정렬
    answer.sort()
    final = list(map(lambda x: x[-2:],answer))
    final_answer = list(map(lambda x: x[-1],final))
        
    return final_answer
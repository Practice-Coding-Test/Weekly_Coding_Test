def solution(weights, head2head):
    
    #인원수 n, 리스트 result, answer 선언
    n= len(weights)
    result,answer=[],[]
    
    #인원수 만큼 반복
    for i in range (n):    
        #선수마다 이긴 횟수, 진 횟수 카운트
        win= head2head[i].count('W')
        lose= head2head[i].count('L')
        
        #조건2) 자신보다 무거운 복서를 이긴 횟수 변수 선언
        heavy_win= 0
        
        #win+lose가 0이면 모두 'N'인경우=> 승률 0으로 처리
        if (win+lose) == 0: 
            win_rate= 0     
        else:
            #승률 계산
            win_rate= win / (win+lose)
        
        for j in range(n):
            #자기 자신과 싸운 경우인 인덱스는 제외
            if i == j: 
                continue
            #이기고 + 자신보다 몸무게가 무거운 복서인 경우 체크
            if head2head[i][j]=='W' and weights[i] < weights[j]:
                heavy_win += 1
        
        #승률, 무거운 선수 이긴 횟수, 몸무게, 선수 번호 순으로 result에 저장
        result.append([-win_rate, -heavy_win, -weights[i],i+1])
    
    #정렬 후 순서대로 선수번호만 answer에 저장해 반환
    result.sort()
    answer = [x[-1] for x in result]
    return answer
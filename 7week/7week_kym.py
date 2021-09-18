def solution(enter, leave):
    answer = [0]*len(enter)
    conference,out = [],[]
    
    for e,l in zip(enter,leave):
        answer[e-1]=len(conference)   # 현재 들어가는 사람은 안에 있는 사람 전부 만남
        
        conference.append(e)
        out.append(l)  
        
        for r in conference[:-1]: # 자기 자신 빼고 
            answer[r-1]+=1  # 안에 있던 사람들은 현재 들어가는 사람 만남
        while out and out[0] in conference:
            conference.remove(out.pop(0))   # 순서대로 나감
    return answer
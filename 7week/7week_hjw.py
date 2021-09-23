#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)] #1로 시작하는 인원수에 맞춰 추출
    room = []
    e_index = 0
    l_index = 0
    
    while e_index < len(enter) or l_index < len(leave):
        if leave[l_index] not in room:
            answer[enter[e_index]]=room[:]
            room.append(enter[e_index])
            e_index += 1
        else:
            room.remove(leave[l_index])
            l_index += 1
    for idx, person in enumerate(answer): # 각 사람에게 서로 만났다는 정보가 저장되어 있어야 함(만난사람 조합 저장)
        for p in person:
            answer[p].append(idx)
    return [len(set(i)) for i in answer][1:] 


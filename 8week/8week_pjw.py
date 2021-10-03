#!/usr/bin/env python
# coding: utf-8

# In[80]:


def solution(sizes):
    total = sum(sizes, [])
    list1 = []
    list2 = []
    if total.index(max(total)) % 2 == 0:
        for i in range(len(sizes)):
            if sizes[i][0] <= sizes[i][1]:
                a = [sizes[i][1], sizes[i][0]]
                list1.append(a)
            else:
                a = [sizes[i][0], sizes[i][1]]
                list1.append(a)
        for k in range(len(list1)):
            list2.append(list1[k][1])
        
    else:
        for i in range(len(sizes)):
            if sizes[i][1] <= sizes[i][0]:
                a = [sizes[i][1], sizes[i][0]]
                list1.append(a)
            else:
                a = [sizes[i][0], sizes[i][1]]
                list1.append(a)
        for k in range(len(list1)):
            list2.append(list1[k][0])
    answer = max(total) * max(list2)
    
    return answer


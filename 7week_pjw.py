#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 함수 만들기
def solution(enter, leave):
    set1 = set()
    for i in enter:
        for k in enter:
            if k != i and enter.index(i) < enter.index(k):
                set1.add((i,k))
                
    set2 = set()
    for m in leave:
        for n in leave:
            if m != n and leave.index(m) > leave.index(n):
                set2.add((m,n))
                
    first = []
    for a in set1:
        for b in set2:
            if a == b:
                first.append(a)
                
    set3 = set()
    for i in enter:
        for k in enter:
            for j in enter:
                if i != k and i != j and j != k:
                    if enter.index(i) < enter.index(k) < enter.index(j):
                        set3.add((i,k))
                        
    set4 = set()
    for m in leave:
        for n in leave:
            for v in leave:
                if m != n and m != v and n != v:
                    if leave.index(n) > leave.index(m) > leave.index(v):
                        set4.add((m,n))
                        
    second = []
    for a in set3:
        for b in set4:
            if a == b:
                second.append(a)
                
    final = first + second
    f_final = sum(final, ())
    
    ans = []
    for i in range(1,len(enter)+1):
        ans.append(f_final.count(i))
        
    return ans


# In[ ]:





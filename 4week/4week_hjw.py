#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(table, languages, preference):
    answer = ''
    result = []
    for tab in range(len(table)):
        result.append((table[tab].split(' ')[0], sum([(6-i)*preference[l] for l in range(len(languages)) for i, t in enumerate(table[tab].split(' ')) if languages[l] == t])))
    return max(dict(sorted(dict(result).items())), key=dict(sorted(dict(result).items())).get)


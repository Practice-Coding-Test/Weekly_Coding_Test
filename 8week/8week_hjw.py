#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(sizes):
    temp = [(max(size), min(size)) for size in sizes]
    return max(temp, key=lambda item: item[0])[0] * max(temp, key=lambda item: item[1])[1]


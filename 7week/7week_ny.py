# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy as np
from random import *

start = 1
end = 10

enter, leave = list(range(start, end)), list(range(start, end))
np.random.shuffle(enter)
np.random.shuffle(leave)
print('enter: ', enter)
print('leave: ', leave)


def solution(enter, leave):
    answer = []
    for i in range(1,len(enter)+1):
        last_idx = []
        for j in range(1,len(enter)+1):
            if (enter.index(i) < enter.index(j)) and (leave.index(i) > leave.index(j)):
                last_idx.append(j)
            if (enter.index(i) > enter.index(j)) and (leave.index(i) < leave.index(j)):
                last_idx.append(j)

        answer.append(len(last_idx))
    return(answer) 
    
solution(enter,leave)


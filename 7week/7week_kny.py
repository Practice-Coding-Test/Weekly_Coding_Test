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

def solution(enter, leave):
    answer, arr = [set() for _ in range(len(enter))], []
    for e in enter:
        arr.append(e)
        for v in arr:
            answer[v-1] |= set(arr)
        while leave and leave[0] in arr:
            arr.remove(leave[0])
            leave.pop(0)
    answer = [len(a)-1 for a in answer]
    return answer    

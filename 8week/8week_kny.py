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

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


def solution(sizes):
    w, h = [0]*len(sizes), [0]*len(sizes)
    for i in range(len(sizes)):
        w[i], h[i] = min(sizes[i]), max(sizes[i])
    answer = max(w)*max(h)
    return answer

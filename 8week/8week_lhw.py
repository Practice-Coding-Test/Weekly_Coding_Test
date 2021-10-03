import pandas as pd

def solution(sizes):
    size_mat = pd.DataFrame(sizes)
    first_order = [0]*len(size_mat)
    second_order = [0]*len(size_mat)
    for i in range(len(size_mat)):
        first_order[i] = max(size_mat.iloc[i])
        second_order[i] = min(size_mat.iloc[i])
    answer = max(first_order) * max(second_order)
    return answer

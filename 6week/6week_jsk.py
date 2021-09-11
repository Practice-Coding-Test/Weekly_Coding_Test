import numpy as np
import pandas as pd


def solution(weights, head2head):
    winning = []
    over_weight = []
    for idx, weight in enumerate(weights):
        # winning rate
        if len(head2head[idx])-head2head[idx].count('N') != 0:
            winning.append(float(head2head[idx].count(
                'W')/(len(head2head[idx])-head2head[idx].count('N'))))
        else:
            winning.append(0)
        # winning count over own weight
        over = 0
        for win in np.where(np.array(list(head2head[idx])) == 'W')[0]:
            if weights[win] > weights[idx]:
                over += 1
        over_weight.append(over)
        # give point according the 4 conditions
        # give weight of 1e+4 to make conditions independent
    point = pd.Series(winning).rank(method="min")*1e+8 + pd.Series(over_weight).rank(method="min") * \
        1e+4 + pd.Series(weights).rank(method="min") + \
        (np.arange(len(weights))[::-1])*1e-4
    # answer list: rank index accroding the point
    answer = list(np.argsort(point)[::-1] + 1)
    return answer

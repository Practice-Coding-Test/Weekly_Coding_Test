#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(weights, head2head):
    answer = []

    for i in range(len(weights)):
        # 1. 승률 계산
        win_rate = [0 if head2head[i].count('W') == 0 else head2head[i].count('W') / (
                    head2head[i].count('W') + head2head[i].count('L'))]

        # 2. 자기보다 무거운 복서를 이긴 횟수
        heavy = [j for j in range(len(weights)) if weights[i] < weights[j]]
        heavy_win = len([k for k in heavy if head2head[i][k] == 'W'])

        answer.append((win_rate, heavy_win, weights[i], i))

    # 3. 순위 매기기
    result = sorted(answer, key=lambda x: (x[0], x[1], x[2], -x[3]), reverse=True)

    return [r[-1] + 1 for r in result]


def solution(enter,leave):
    sub = []
    ans = [0] * len(enter)      #정답
    met = []        #기존에 만났던 사람
    for i in enter:
        sub.append(i)
        if i != leave[0]:
            pass
        else:
            minus = [i for i in sub if i in met]
            for j in sub:
                if j in met:
                    ans[j - 1] += len(sub) -len(minus)      #기존에 만났던 사람은 빼준다.
                else:
                    ans[j - 1] += len(sub) - 1
                    met.append(j)
            leave.pop(0)
            sub.pop()

            for _ in range(len(sub)):
                for i in sub:
                    if i == leave[0]:
                        sub.remove(i)
                        leave.pop(0)
    return ans  

def solution(sizes):
    w, h = [], []

    for item in sizes:
        if item[0] > item[1]:
            item[0], item[1] = item[1], item[0]
        w.append(item[1])
        h.append(item[0])

    answer = max(w)*max(h)

    return answer

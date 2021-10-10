def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        tmp = wires.copy()
        a = []
        b = []
        a.append(tmp[i][0])
        b.append(tmp[i][1])

        tmp.pop(i)
        j = 0
        while (len(tmp)):
            if (tmp[j][0] in a) or (tmp[j][1] in a):
                if (tmp[j][0] not in a):
                    a.append(tmp[j][0])
                else:
                    a.append(tmp[j][1])
                tmp.pop(j)
                j = j - 1
            elif (tmp[j][0] in b) or (tmp[j][1] in b):
                if (tmp[j][0] not in b):
                    b.append(tmp[j][0])
                else:
                    b.append(tmp[j][1])
                tmp.pop(j)
                j = j - 1

            j = j + 1
            if (j == len(tmp)):
                j = 0

        cnt = abs(len(a) - len(b))
        if (len(tmp) == 0) & (answer > cnt):
            answer = cnt

    return answer

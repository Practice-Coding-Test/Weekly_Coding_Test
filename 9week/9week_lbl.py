def solution(n, wires):
    answer = 999
    dic = {}
    for i in range(1,n+1):
        dic[i] = []
    for idx in range(n-1):
        a,b = wires[idx]
        dic[a].append(b)
        dic[b].append(a)
    for w in wires:
        a = dic[w[0]].copy()
        if len(dic[w[0]]) > len(dic[w[1]]):
            a = dic[w[1]].copy()
        a_cnt = 0
        visited = a.copy()
        visited.extend([w[0],w[1]])
        while a:
            target = a.pop()
            if target == w[0] or target == w[1]:
                continue
            a_cnt += 1
            for ele in dic[target]:
                if ele not in visited:
                    a.append(ele)
                    visited.append(ele)
        answer = min(abs(n - a_cnt -2 - a_cnt),answer)
        
    return answer

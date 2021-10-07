import sys
from collections import deque

def bfs(node, graph):
    que = deque([node])
    visit = [False] * (101)
    cnt = 0

    visit[node] = True
    while que:
        v = que.popleft()
        cnt+=1
        for i in graph[v]:
            if visit[i] == True:
                continue
            que.append(i)
            visit[i] = True
            
    return cnt
    
def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    answer= 1e9
    
    #인접리스트 tree 생성
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
        
    #연결된 송전탑들을 하나씩 끊기- 개수 탐색- 다시 연결(복구) 반복
    for wire in wires:
        tree[wire[0]].remove(wire[1])
        tree[wire[1]].remove(wire[0])
        
        answer = min(answer, abs(bfs(wire[0], tree) - bfs(wire[1], tree)));

        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    
    return answer
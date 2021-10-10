Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def solution(N, wires):
    answer = N
    tree = {i : set() for i in range(1, N+1)}
    for a,b in wires:
        tree[a].add(b)
        tree[b].add(a)
    for a,b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        result = abs(2*bfs(a, tree)-N)
        tree[a].add(b)
        tree[b].add(a)
        answer = min(answer, result)
    return answer

def bfs(start, tree):
    queue = [start]
    marked = {start}
    while queue:
        v = queue.pop(0)
        for w in tree[v]:
            if w not in marked:
                queue.append(w)
                marked.add(w)
    return len(marked)

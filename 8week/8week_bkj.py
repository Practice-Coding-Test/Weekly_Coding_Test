Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(sizes):
    h = 0
    w = 0
    
    for i in sizes:
        if h < min(i[0], i[1]) : h = min(i[0], i[1])
        if w < max(i[0], i[1]) : w = max(i[0], i[1])
    
    answer = w*h
    return answer

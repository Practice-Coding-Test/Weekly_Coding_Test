def solution(sizes):
    w,h = 0,0
    for size in sizes:
        a,b = size[0],size[1]
        if a>b: a,b = b,a
        w = max(w,a)
        h = max(h,b)
    return w*h

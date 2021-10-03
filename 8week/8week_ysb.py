def solution(sizes):
    w,h=0,0
    for i in sizes:
        if sorted(i,reverse=True)[0]>w:
            w=sorted(i,reverse=True)[0]
        if sorted(i,reverse=True)[1]>h:
            h=sorted(i,reverse=True)[1]
    return w*h
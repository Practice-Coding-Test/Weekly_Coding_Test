def solution(sizes):
    width = 0
    height = 0
    for size in sizes:
        # set larger element as width, smaller as height
        if size[0] >= size[1]:
            w = size[0]
            h = size[1]
        else:
            w = size[1]
            h = size[0]
        # find max width & height
        if width < w:
            width = w
        if height < h:
            height = h
    answer = width*height
    return answer

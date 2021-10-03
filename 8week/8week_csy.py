def solution(sizes):
    weight = 0
    height = 0
    
    for w,h in sizes:
        weight = max(weight, w, h) # 큰 것 중 가장 큰 것
        height = max(height, min(w,h)) # 작은 것 중 가장 큰 것
        
    return weight*height

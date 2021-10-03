def solution(sizes):
    # 항상 left >= right
    left = 0; right = 0;
    for size in sizes:
        tmp_left, tmp_right = max(size),min(size)
        if left < tmp_left:
            left = tmp_left
        if right < tmp_right:
            right = tmp_right
    answer = left * right
    return answer

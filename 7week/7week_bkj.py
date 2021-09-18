Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(enter, leave):   
    arr = [] 
    answer = [0] * len(enter)
    enter_idx, leave_idx = [0] * 2
    
    while True:
        if leave_idx == len(enter): 
            break
        while arr and leave_idx < len(enter):
            try:
                x = arr.index(leave[leave_idx])
                del arr[x]
                leave_idx += 1
            except:
                break

        if enter_idx < len(enter):
            arr.append(enter[enter_idx])
            enter_idx += 1
        
        if len(arr) > 1:
            for p in arr: answer[p-1] += 1 if answer[p-1] > 0 else len(arr) - 1
            
    return answer

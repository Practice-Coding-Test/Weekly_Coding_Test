def solution(price, money, count):
    hap = 0
    for i in range(1, count+1):
        hap = hap + price*i
    if hap > money:
        answer = hap - money
    else:
        answer = 0

    return answer
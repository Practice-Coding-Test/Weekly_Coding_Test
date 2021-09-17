def solution(price, money, count):
    money = money - price * count * (count + 1) / 2

    if money >= 0:
        answer = 0
    else:
        answer = -1 * money

    return answer 

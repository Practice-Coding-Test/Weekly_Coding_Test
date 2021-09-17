def solution(price, money, count):
    money = money - price * count * (count + 1) / 2

    if money >= 0:
        answer = 0
    else:
        answer = -1 * money

<<<<<<< HEAD
    return answer
=======
    return answer 
>>>>>>> d563b7985ce2d32b3f7c111bc86c182449e250fe

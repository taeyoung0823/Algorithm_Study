
    

def solution(price, money, count):
    result = 0
    for i in range(count+1):
        result += i
    answer = result*price-money
    if answer <0:
        return 0
    return answer
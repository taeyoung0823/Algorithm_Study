def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        found = False

        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                answer.append(j-i)
                found = True
                break
        if not found:
            answer.append(len(prices)-i-1)
    answer.append(0)
    return answer
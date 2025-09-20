def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        text = t[i:i+len(p)]
        if text <= p:
            answer +=1
    return answer
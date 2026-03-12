def solution(brown, yellow):
    answer = []
    ent = brown+yellow
    for i in range(1,int(ent**(1/2))+1):
        if ent%i==0:
            if (i+(ent/i)-2)*2==brown:
                answer.append(i)
                answer.append(ent/i)
    answer = sorted(answer,reverse=True)
    return answer
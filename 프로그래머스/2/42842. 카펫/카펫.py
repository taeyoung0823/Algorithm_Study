def solution(brown, yellow):
    answer = []
    all = brown+yellow
    for i in range(1,int(all**(1/2))+1):
        if all%i==0:
            if (i+all/i-2)*2==brown:
                answer.append(i)
                answer.append(all/i)
    answer = sorted(answer,reverse=True)
    return answer
def solution(k, score):
    answer = []
    lst=[]
    for i in range(len(score)):
        lst.append(score[i])
        lst.sort()
        if len(lst)<=k:
            answer.append(lst[0])
        else:
            answer.append(lst[len(lst)-k])
    return answer
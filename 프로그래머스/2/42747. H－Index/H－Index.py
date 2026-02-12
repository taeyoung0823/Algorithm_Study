def solution(citations):
    answer = 0
    citations.sort()
    if len(citations)<=citations[0]:
        return len(citations)
    if len(citations)==1 and citations[0]==0:
        return 0
    for i in range(1,len(citations)):
        for j in range(len(citations)):
            if i <= citations[j]:
                if i <= len(citations[j:]):
                    answer = i
                    break
    return answer
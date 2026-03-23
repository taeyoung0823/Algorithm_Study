def solution(n, lost, reserve):
    
    lst=[]
    
    for i in range(len(lost)):
        if lost[i] in reserve:
            lst.append(lost[i])
    
    for i in range(len(lst)):
        lost.remove(lst[i])
        reserve.remove(lst[i])
        
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            answer+=1
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            answer+=1
            reserve.remove(lost[i]+1)
    return answer
def solution(food):
    lst=[]
    rev=''
    answer = ''
    
    for i in range(len(food)):
        lst.append(food[i]//2)
    
    for i in range(1,len(food)):
        answer += str(i) * lst[i]
    
    for i in range(len(answer)):
        rev += answer[-1-i]
    
    answer+='0'
    answer+=rev
    
    return answer
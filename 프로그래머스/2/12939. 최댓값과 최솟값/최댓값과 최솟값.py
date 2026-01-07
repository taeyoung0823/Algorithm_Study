def solution(s):
    answer = ''
    a=[]
    for i in s.split():
        a.append(int(i))
    
    answer+=str(min(a))
    answer+=' '
    answer+=str(max(a))
    
    return answer
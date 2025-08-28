def solution(n):
    answer = 0
    result=""
    lst=[]
    
    for i in range(len(str(n))):
        lst += str(n%10)
        n = n//10
        lst.sort(reverse=True)
        
    for i in range(len(lst)):
        result += lst[i]
    
    return int(result)
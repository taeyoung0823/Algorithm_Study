def solution(s):
    answer = True
    for i in range(len(s)):
        if s[i].isalpha():
            return False
        
    if len(s)!=4:
        if len(s)!=6:
            return False
    return answer
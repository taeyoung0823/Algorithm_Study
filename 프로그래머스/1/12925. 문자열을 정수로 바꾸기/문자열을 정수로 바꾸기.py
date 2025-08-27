def solution(s):
    answer = 0
    num=[1,2,3,4,5]
    if s[0]=='-' or s[0]=='+':
        answer=s[0]+s[1:]
    else:
        answer=s
    return int(answer)
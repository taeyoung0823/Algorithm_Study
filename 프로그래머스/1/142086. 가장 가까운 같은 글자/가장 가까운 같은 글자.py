def solution(s):
    answer = []
    lst={}
    for i in range(len(s)):
        if s[i] in lst:
            answer.append(i-lst[s[i]])
        else:
            answer.append(-1)
        lst[s[i]]=i
    return answer
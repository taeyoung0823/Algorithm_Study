def solution(s):
    answer = ''
    count=0
    for i in range(len(s)):
        if count%2==0:
            if s[i]!=' ':
                answer+=s[i].upper()
                count+=1
            else:
                answer+=s[i]
        elif count%2!=0:
            if s[i]==' ':
                answer+=s[i]
                count=0
            else:
                answer+=s[i].lower()
                count+=1
    return answer
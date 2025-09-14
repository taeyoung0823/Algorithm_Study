def solution(s):
    answer = ''
    lower=''
    upper=''
    
    for i in range(len(s)):
        if s[i].isupper():
            upper+=s[i]
        else:
            lower+=s[i]
    print(upper)
    print(lower)
    upper=''.join(sorted(upper,reverse=True))
    lower=''.join(sorted(lower,reverse=True))
    
    answer= lower+upper
    return answer
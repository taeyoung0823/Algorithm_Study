def solution(s):
    answer = True
    cnt1=s.count('(')
    cnt2=s.count(')')
    
    if s[0] != '(':
        return False
    elif s[-1] != ')':
        return False
    elif cnt1!=cnt2:
        return False
    else:
        cnt1=0
        cnt2=0
        for i in range(len(s)):
            if s[i]=='(':
                cnt1+=1
            if s[i]==')':
                cnt2+=1
            if cnt2>cnt1:
                return False
    return True
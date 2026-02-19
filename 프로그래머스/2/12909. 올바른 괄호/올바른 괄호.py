def solution(s):
    stack=[]
    answer = True
    
    if s[0]==')' or not s:
        return False
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        if s[i]==')':
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    return False

    return True
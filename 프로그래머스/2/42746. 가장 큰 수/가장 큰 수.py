from functools import cmp_to_key

def solution(numbers):
    def cmp(a, b):
        a, b = str(a), str(b)
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    answer=''
    s = sorted(numbers, key=cmp_to_key(cmp))
    for i in range(len(s)):
        answer+=str(s[i])
    if answer[0]=='0':
        return '0'
    else:
        return answer
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if prime(i)==1:
            answer+=1
    return answer

def prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 2
    return 1
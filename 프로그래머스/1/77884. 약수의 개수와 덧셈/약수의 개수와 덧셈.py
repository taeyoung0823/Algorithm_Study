def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if yak(i)%2==0:
            answer+=i
        else:
            answer-=i
    return answer

def yak(n):
    cnt=0
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            if i*i==n:
                cnt+=1
            else:
                cnt+=2
    return cnt
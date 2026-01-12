def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*(2*j+i-1)/2==n:
                answer+=1
                break
            if i*(2*j+i-1)/2>n:
                break
    return answer
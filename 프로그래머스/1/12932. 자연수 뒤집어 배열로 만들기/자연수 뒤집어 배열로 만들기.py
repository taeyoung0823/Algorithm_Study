def solution(n):
    answer = []
    for i in range(len(str(n))):
        num=n%10
        answer.append(num)
        n=n//10
    return answer
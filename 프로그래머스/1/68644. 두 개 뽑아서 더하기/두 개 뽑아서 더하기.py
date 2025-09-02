def solution(numbers):
    answer = []
    lst=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    lst=sorted(list(set(answer)))
    return lst
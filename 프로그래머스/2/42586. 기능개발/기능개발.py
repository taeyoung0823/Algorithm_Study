def solution(progresses, speeds):
    answer = []
    count=0
    
    while len(progresses):
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
        if progresses[0]>=100:
            count+=1
            for i in range(1,len(progresses)):
                if progresses[i]>=100:
                    count+=1
                else:
                    break
            del progresses[:count]
            del speeds[:count]
            answer.append(count)
            count=0
    return answer
def solution(N, stages):
    answer = []
    player=len(stages)
    failure={}
    
    for i in range(1,N+1):
        if player==0:
            failure[i]=0
        else:
            failure[i]=stages.count(i)/player
            player-=stages.count(i)
                
    answer = sorted(failure, key=lambda x : failure[x], reverse=True)
    return answer
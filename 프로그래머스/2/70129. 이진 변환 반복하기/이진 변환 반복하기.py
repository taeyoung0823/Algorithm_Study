def solution(s):
    answer = []
    cnt=0
    n=0
    
    while s != "1":
        zero=s.count("0")
        cnt+=zero
        s=s.replace("0","")
        s=bin(len(s))[2:]
        n+=1
    
    answer.append(n)
    answer.append(cnt)
    
    return answer
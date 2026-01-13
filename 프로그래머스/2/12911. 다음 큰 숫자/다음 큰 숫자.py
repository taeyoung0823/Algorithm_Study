def solution(n):
    answer = 0
    bin_n = str(bin(n)[2:])
    count = bin_n.count('1')
    
    for i in range(n+1,1000000):
        if str(bin(i)[2:]).count('1')==count:
            answer+=i
            break
    
    return answer
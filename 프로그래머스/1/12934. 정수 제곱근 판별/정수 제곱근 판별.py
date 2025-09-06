def solution(n):
    num=0
    i=1
    while 1:
        num=i*i
        if num==n:
            return (i+1)*(i+1)
        if num>n:
            return -1
        i=i+1
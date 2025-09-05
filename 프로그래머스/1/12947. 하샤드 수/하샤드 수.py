def solution(x):
    sum=0
    num=x
    for i in range(len(str(x))):
        sum+=x%10
        x=x//10
    if num%sum==0:
        return True
    else:
        return False
def solution(a, b):
    answer = ''
    num=0
    for i in range(a):
        if i<8:
            if i%2!=0:
                b+=31
            elif i==2:
                b+=29
            else:
                b+=30
        else:
            if i%2!=0:
                b+=30
            else:
                b+=31
    num = b%7
    if num==0:
        answer+='TUE'
    if num==1:
        answer+='WED'
    if num==2:
        answer+='THU'
    if num==3:
        answer+='FRI'
    if num==4:
        answer+='SAT'
    if num==5:
        answer+='SUN'
    if num==6:
        answer+='MON'
    return answer
def solution(sizes):
    answer=0
    w=0
    h=0
    for rec in sizes:
        if rec[0]<rec[1]:
            rec[0],rec[1]=rec[1],rec[0]
        if w<rec[0]:
            w=rec[0]
        if h<rec[1]:
            h=rec[1]
    answer=w*h
    return answer
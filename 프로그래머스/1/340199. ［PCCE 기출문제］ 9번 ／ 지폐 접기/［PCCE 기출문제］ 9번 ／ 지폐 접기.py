def solution(wallet, bill):
    answer = 0
    wallet = sorted(wallet)
    bill = sorted(bill)
    while 1:
        if wallet[0]<bill[0] or wallet[1]<bill[1]:
            bill[1]=bill[1]//2
            bill=sorted(bill)
            answer+=1
        else:
            return answer
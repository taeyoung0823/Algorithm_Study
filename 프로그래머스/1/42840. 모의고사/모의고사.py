def solution(answers):
    answer = []
    cnt1=0
    cnt2=0
    cnt3=0
    lst1=[1,2,3,4,5]*len(answers)
    lst2=[2,1,2,3,2,4,2,5]*len(answers)
    lst3=[3,3,1,1,2,2,4,4,5,5]*len(answers)
    
    for i in range(len(answers)):
        if answers[i]==lst1[i]:
            cnt1+=1
        if answers[i]==lst2[i]:
            cnt2+=1
        if answers[i]==lst3[i]:
            cnt3+=1
    
    if max(cnt1,cnt2,cnt3)==cnt1:
        answer.append(1)
    if max(cnt1,cnt2,cnt3)==cnt2:
        answer.append(2)
    if max(cnt1,cnt2,cnt3)==cnt3:
        answer.append(3)
        
    
    return answer
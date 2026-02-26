def solution(answers):
    answer = []
    ans_1=[1,2,3,4,5]*len(answers)
    ans_2=[2,1,2,3,2,4,2,5]*len(answers)
    ans_3=[3,3,1,1,2,2,4,4,5,5]*len(answers)
    
    max_correct=0
    cor_1=0
    cor_2=0
    cor_3=0
    
    for i in range(len(answers)):
        if ans_1[i]==answers[i]:
            cor_1+=1
        if ans_2[i]==answers[i]:
            cor_2+=1
        if ans_3[i]==answers[i]:
            cor_3+=1
    max_correct=max(cor_1,cor_2,cor_3)
    
    if max_correct==cor_1:
        answer.append(1)
    if max_correct==cor_2:
        answer.append(2)
    if max_correct==cor_3:
        answer.append(3)
    
    
    
    
    return answer
def solution(name, yearning, photo):
    answer = []
    dico = {name[i]:yearning[i] for i in range(0, len(name))}
    sc = 0
    for p in photo:
        for n in p :
            if n in dico:
                sc += dico[n]
        answer.append(sc)
        sc = 0
    return answer
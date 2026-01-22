def solution(clothes):
    counts = {}  

    for name, kind in clothes:
        counts[kind] = counts.get(kind, 0) + 1

    answer = 1
    for c in counts.values():
        answer *= (c + 1)

    return answer - 1

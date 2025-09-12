def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        merged = format(arr1[i] | arr2[i], 'b').zfill(n)
        
        line = merged.replace('1', '#').replace('0', ' ')
        answer.append(line)

    return answer

def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        prev = ""
        while len(babbling[i]) > 0:
            if babbling[i].startswith("aya") and prev != "aya":
                babbling[i] = babbling[i][3:]
                prev = "aya"
            elif babbling[i].startswith("ye") and prev != "ye":
                babbling[i] = babbling[i][2:]
                prev = "ye"
            elif babbling[i].startswith("woo") and prev != "woo":
                babbling[i] = babbling[i][3:]
                prev = "woo"
            elif babbling[i].startswith("ma") and prev != "ma":
                babbling[i] = babbling[i][2:]
                prev = "ma"
            else:
                break

        if len(babbling[i]) == 0:
            answer += 1

    return answer

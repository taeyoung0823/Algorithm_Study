def solution(n, m, section):
    count = 0
    last_painted = 0

    for pos in section:
        if pos > last_painted:
            count += 1
            last_painted = pos + m - 1

    return count
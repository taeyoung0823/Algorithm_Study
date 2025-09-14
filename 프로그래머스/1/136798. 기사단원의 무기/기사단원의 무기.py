def solution(number, limit, power):
    weapon = []
    a = 0

    for i in range(1, number + 1):
        p = pris(i)
        if p <= limit:
            a += p
        else:
            a += power

    return a


def pris(n):
    c = 0

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c += 1
            if n // i != i:
                c += 1

    return c
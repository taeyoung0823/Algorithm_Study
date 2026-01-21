def solution(phone_book):
    phone_book.sort(key=len)
    s = set(phone_book)
    for num in phone_book:
        for k in range(1, len(num)):
            if num[:k] in s:
                return False
    return True
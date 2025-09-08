def solution(phone_number):
    answer = ''
    num = len(phone_number)-4
    answer += '*' * num
    answer += phone_number[num:]
    return answer
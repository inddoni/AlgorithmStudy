def solution(phone_number):
    if len(phone_number) < 4 or len(phone_number) > 20:
        answer = False
    else:
        answer = ''
        for i in range(0, len(phone_number)) :
            if(i < len(phone_number)-4) :
                answer += '*'
            else :
                answer += phone_number[i]
    return answer

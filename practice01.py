def solution(s):
    if len(s) == 4 or len(s) == 6 :
        answer = s.isnumeric()
    else :
        answer = False
    return answer

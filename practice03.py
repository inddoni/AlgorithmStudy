def solution(s):
    ques = s.lower()
    p, y = 0, 0
    for i in range(0,len(ques)) :
        if ques[i] == 'p':
            p += 1
        elif ques[i] == 'y':
            y += 1
    return p == y


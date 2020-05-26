import re
def solution(s):
    answer = []

    findCount = 0
    s = re.split(",|{|}", s)
    blankCount = 0
    tupList = []
    tup = []

    for i in range(len(s)) :
        if s[i] == '':
            blankCount += 1
            if findCount > 0 and tup:
                tupList.append(tup)
                tup = []
        else :
            if blankCount == 2 :
                tup.append(s[i])
            if i < len(s)-1 :
                if s[i+1] == '' :
                    findCount += 1
                    blankCount = 0

    num = len(tupList) #4개
    for i in range(num) :
        for j in tupList :
            if len(j) == i+1 :
                for k in j :
                    if int(k) not in answer :
                        answer.append(int(k))

    return answer





s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
result = solution(s)
print(result)
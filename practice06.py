def solution(s):
    count = 0
    result = ""
    for i in s.split(' ') :
        for j in list(i) :
            count += 1
            if count % 2 == 1 :
                result += j.upper()
            else :
                result += j.lower()
        count = 0
        result += " "
    return result.rstrip()

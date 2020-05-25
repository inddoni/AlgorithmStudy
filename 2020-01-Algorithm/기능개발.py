import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    num = len(progresses)
    dayslist = deque()

    for i in range(num) :
        pro = 100 - progresses[i]
        days = pro / speeds[i]
        if str(type(days)) == "<class 'float'>" :
            days = math.ceil(days)

        dayslist.append(days)

    count = 1
    first = dayslist.popleft()

    while len(dayslist) != 0 :
        if first >= dayslist[0] :
            count += 1
            dayslist.popleft()
        else :
            answer.append(count)
            count = 1
            first = dayslist.popleft()

    total = 0
    for i in answer :
        total += i

    if total < num :
        answer.append(count)


    return answer









p = [99, 99, 99, 99, 99]
s = [3, 3, 3, 3, 3]
result = solution(p, s)
print(result)
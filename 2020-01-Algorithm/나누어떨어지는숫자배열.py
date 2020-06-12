def solution(arr, divisor):
    answer = []
    div = 0
    for i in arr :
        div = i // divisor
        if i == (div * divisor) :
            answer.append(i)

    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer



arr = [2, 36, 1, 3]
divisor = 1
ans = solution(arr, divisor)
print(ans)
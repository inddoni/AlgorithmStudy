def solution(board, moves):
    answer = 0
    pickList = []
    for i in moves : #i = 1
        pick = 0
        for j in range(0, len(board)) : #j = 0~4
            if board[j][i-1] != 0 :
                pick = board[j][i-1]
                board[j][i-1] = 0
                break
            else :
                continue

        if pick != 0 :
            if len(pickList) != 0 : #리스트가 비어있지 않으면
                if pickList[-1] != pick :
                    pickList.append(pick)
                else : # 두 인형이 같으면 기존 리스트에 값 삭제
                    del pickList[-1]
                    answer += 2
            else :
                pickList.append(pick)


    return answer
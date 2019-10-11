def solution(participant, completion):
    completion.append('ㄱ')
    for nameP, nameC in zip(sorted(participant), sorted(completion)):
        if nameP != nameC : return nameP

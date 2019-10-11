def solution(s):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a *= (len(s) // len(a)) + 1
    b *= (len(s) // len(b)) + 1
    c *= (len(s) // len(c)) + 1

    scores = [0, 0, 0]
    for i in range(0,len(s)) :
        if a[i] == s[i] : scores[0] += 1
        if b[i] == s[i] : scores[1] += 1
        if c[i] == s[i] : scores[2] += 1

    winner = []
    for i, s in enumerate(scores) :
        if s == max(scores) :
            winner += [i+1]
            
    return winner

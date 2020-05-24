
def gcd(a,b):
    return b if (a==0) else gcd(b%a,a)
def solution(w,h):
    return w*h-w-h+gcd(w,h)



wid = 8
hig = 12
re = solution(wid, hig)
print(re)
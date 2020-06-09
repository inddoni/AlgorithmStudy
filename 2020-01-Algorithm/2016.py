import datetime


def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return week[datetime.date(2016, a, b).weekday()]



a = 4
b = 26
day = solution(a, b)
print(day)
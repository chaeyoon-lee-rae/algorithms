"""
https://school.programmers.co.kr/learn/courses/30/lessons/150370

1단계에는 다 이유가 있다. 최소단위로 데이터를 변경하여 간단하게 비교할 수 있는 방법을 먼저 강구해보도록 하자.

다른 사람 솔루션->

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
"""

def solution(today, terms, privacies):
    today_year, today_month, today_date = today.split(".")
    today_year = int(today_year)
    today_month = int(today_month)
    today_date = int(today_date)

    term_dict = {}
    for term in terms:
        kind, duration = term.split(" ")
        duration = int(duration)
        term_dict[kind] = duration

    answer = []
    for idx, privacy in enumerate(privacies):
        privacy_date, each_term = privacy.split(" ")
        each_year, each_month, each_date =  privacy_date.split(".")
        each_year = int(each_year)
        each_month = int(each_month)
        each_date = int(each_date)

        yrs, months = divmod(term_dict[each_term], 12)
        each_year += yrs
        each_month += months
        if each_month > 12:
            each_year += 1
            each_month %= 12

        each_date -= 1
        if each_date == 0:
            each_month -= 1
            each_date = 28
            if each_month == 0:
                each_year -= 1
                each_month = 12

        if today_year > each_year:
            answer.append(idx+1)
        elif today_year == each_year:
            if today_month > each_month:
                answer.append(idx+1)
            elif today_month == each_month:
                if today_date > each_date:
                    answer.append(idx+1)

    return answer

if __name__ == "__main__":
    today = "2020.01.01"
    terms = ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    answer = solution(today, terms, privacies)
    print(answer)
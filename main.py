from datetime import datetime

def get_days_from_today(date):
    from_date = datetime.strptime(date, "%Y-%m-%d")
    now = datetime.now()
    result = now.toordinal() - from_date.toordinal()
    return result

date = input("Введіть дату в форматі РРРР-ММ-ДД")
get_days_from_today(date)

print(get_days_from_today(date))
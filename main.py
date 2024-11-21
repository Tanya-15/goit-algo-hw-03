from datetime import datetime

def get_days_from_today(date):
    try:
        from_date = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.now()
        result = now.toordinal() - from_date.toordinal()
        return result
    except ValueError:
        return "Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД."

date = input("Введіть дату в форматі РРРР-ММ-ДД: ")
result = get_days_from_today(date)

print(result)
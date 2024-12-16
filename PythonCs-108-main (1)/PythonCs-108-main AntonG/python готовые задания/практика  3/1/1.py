from datetime import datetime

def datetime_info(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d-%m-%Y')
        days_russian = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        day_of_week = days_russian[date_obj.weekday()]
        next_year = date_obj.year + 1
        first_day_next_year = datetime(year=next_year, month=1, day=1)
        delta = first_day_next_year - date_obj
        days_until_next_year = delta.days

        return {
            'formatted_date': formatted_date,
            'day_of_week': day_of_week,
            'days_until_next_year': days_until_next_year
        }
    except ValueError:
        return {"error": "Неверный формат даты. Ожидается 'YYYY-MM-DD'."}

if __name__ == "__main__":
    date_input = '2023-12-25'
    result = datetime_info(date_input)
    print(f"Входная дата: {date_input}")
    print("Результат:", result)
    invalid_date_input = '25-12-2023'
    invalid_result = datetime_info(invalid_date_input)
    print(f"\nВходная дата: {invalid_date_input}")
    print("Результат:", invalid_result)

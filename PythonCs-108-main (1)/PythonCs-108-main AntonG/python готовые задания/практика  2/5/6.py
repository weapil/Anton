def tuple_stats(tpl):
    Total_sum = sum(tpl)
    Average = Total_sum / len(tpl)
    Unique_elements = tuple(set(tpl))

    return Total_sum, Average, Unique_elements
def get_tuple_from_input():
    while True:
        try:
            user_input = input("Введите числа через пробел для создания кортежа: ")
            tpl = tuple(map(float, user_input.split()))
            if len(tpl) == 0:
                raise ValueError("Кортеж не должен быть пустым.")
            return tpl
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")
user_tuple = get_tuple_from_input()
total_sum, average, unique_elements = tuple_stats(user_tuple)
print(f"Сумма всех элементов: {total_sum}")
print(f"Среднее значение: {average}")
print(f"Кортеж уникальных элементов: {unique_elements}")
print("\nРазница между словарями, множествами и кортежами:")
print("1. Словари (dict): это коллекции, где каждый элемент представлен парой ключ-значение. Ключи уникальны.")
print("2. Множества (set): это коллекции уникальных элементов, не содержащие дубликатов.")
print("3. Кортежи (tuple): это неизменяемые последовательности элементов. В отличие от списков, кортежи нельзя модифицировать после создания.")

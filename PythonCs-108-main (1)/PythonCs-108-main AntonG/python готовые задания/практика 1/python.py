import random

random_numbers = []
random_numbers = [random.randint(1, 10) for _ in range(10)]
user_input = int(input("Введите число: "))
if user_input in random_numbers:
    print(f"Число {user_input} находится в массиве.")
else:
    print(f"Число {user_input} не находится в массиве.")
print(f"Массив случайных чисел: {random_numbers}")

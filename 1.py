def multiply_func(nums: list[int], factor: int = 2) -> list[int]:
    return [num * factor for num in nums]

multiply_lambda = lambda numbers_list, coefficient=2: list(map(lambda x: x * coefficient, numbers_list))

def get_numbers() -> list[int]:
    while True:
        try:
            user_input = input("Введите числа через пробел: ")
            if not user_input.strip():
                raise ValueError("Список не может быть пустым")
            return [int(num) for num in user_input.split()]
        except ValueError as e:
            print(f"Ошибка: {e}. Вводите только целые числа")

def get_multiplier() -> int:
    while True:
        try:
            user_input = input("Введите множитель (по умолчанию 2): ")
            return int(user_input) if user_input else 2
        except ValueError:
            print("Ошибка: множитель должен быть целым числом")

input_numbers = get_numbers()
input_multiplier = get_multiplier()

print("Результат функции:", multiply_func(input_numbers, input_multiplier))
print("Результат лямбды:", multiply_lambda(input_numbers, input_multiplier))
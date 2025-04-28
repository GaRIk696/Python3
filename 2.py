def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

def get_positive_number(prompt: str) -> float:
    while True:
        num = get_number(prompt)
        if num >= 0:
            return num
        print("Ошибка: число должно быть положительным!")

def get_integer(prompt: str) -> int:
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                return num
            print("Ошибка: число должно быть неотрицательным!")
        except ValueError:
            print("Ошибка: введите целое число!")

def get_number_list(prompt: str) -> list[float]:
    while True:
        try:
            nums = input(prompt).split()
            return [float(num) for num in nums]
        except ValueError:
            print("Ошибка: все элементы должны быть числами!")

def format_result(result) -> str:
    if isinstance(result, float) and result.is_integer():
        return f">>> {int(result)}\n-------------------------"
    return f">>> {result}\n-------------------------"

def calculate_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_sqrt(num: float) -> float:
    if num == 0:
        return 0.0
    guess = num / 2
    for _ in range(20):  # Простая реализация метода Ньютона
        guess = (guess + num / guess) / 2
    return guess

def addition() -> str:
    a = get_number("Первое слагаемое: ")
    b = get_number("Второе слагаемое: ")
    return format_result(a + b)

def subtraction() -> str:
    a = get_number("Уменьшаемое: ")
    b = get_number("Вычитаемое: ")
    return format_result(a - b)

def multiplication() -> str:
    a = get_number("Первый множитель: ")
    b = get_number("Второй множитель: ")
    return format_result(a * b)

def division() -> str:
    print("1. Обычное деление\n2. Остаток от деления\n3. Деление нацело")
    choice = input("Выберите тип деления (1-3): ")

    a = get_number("Делимое: ")
    b = get_number("Делитель: ")

    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")

    if choice == '1':
        return format_result(a / b)
    elif choice == '2':
        return format_result(a % b)
    elif choice == '3':
        return format_result(a // b)
    else:
        raise ValueError("Неверный выбор операции!")

def power() -> str:
    base = get_number("Основание: ")
    exponent = get_number("Показатель: ")
    return format_result(base ** exponent)

def factorial() -> str:
    n = get_integer("Число: ")
    return format_result(calculate_factorial(n))

def average() -> str:
    nums = get_number_list("Введите числа через пробел: ")
    if not nums:
        raise ValueError("Список чисел не может быть пустым!")
    return format_result(sum(nums) / len(nums))

def square_root() -> str:
    num = get_positive_number("Число: ")
    return format_result(calculate_sqrt(num))

OPERATIONS = {
    '1': ("Сложение", addition),
    '2': ("Вычитание", subtraction),
    '3': ("Умножение", multiplication),
    '4': ("Деление", division),
    '5': ("Возведение в степень", power),
    '6': ("Факториал", factorial),
    '7': ("Среднее арифметическое", average),
    '8': ("Квадратный корень", square_root)
}

def main():
    while True:
        print("\nДоступные операции:")
        for key, (name, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("exit - Выход")
        print("-------------------------")

        choice = input("Операция: ").strip().lower()

        if choice == "exit":
            break

        if choice in OPERATIONS:
            try:
                print(OPERATIONS[choice][1]())
            except Exception as e:
                print(f"Ошибка: {e}")
        else:
            print("Неизвестная операция!")

        input("Нажмите Enter чтобы продолжить...")

main()
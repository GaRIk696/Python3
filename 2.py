def get_number(prompt):
    value = input(prompt)
    try:
        num = float(value)
        return num
    except ValueError:
        raise ValueError("Должно быть введено число!")


def get_integer(prompt):
    value = input(prompt)
    try:
        num = int(value)
        if num < 0:
            raise ValueError("Число должно быть неотрицательным!")
        return num
    except ValueError:
        raise ValueError("Должно быть введено целое число!")


def format_result(result):
    if isinstance(result, complex):
        return f">>> {result}\n-------------------------"
    if isinstance(result, float) and result.is_integer():
        return f">>> {int(result)}\n-------------------------"
    return f">>> {result}\n-------------------------"


def calculate_sum():
    a = get_number("Слагаемое 1: ")
    b = get_number("Слагаемое 2: ")
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise ValueError("Оба слагаемых должны быть числами!")
    return format_result(a + b)


def calculate_difference():
    a = get_number("Уменьшаемое: ")
    b = get_number("Вычитаемое: ")
    if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise ValueError("Оба числа должны быть числовыми!")
    return format_result(a - b)


def calculate_product():
    a = get_number("Множитель 1: ")
    b = get_number("Множитель 2: ")
    if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise ValueError("Оба множителя должны быть числами!")
    return format_result(a * b)


def calculate_division():
    print("Виды деления:\n1. Обычное деление\n2. Остаток от деления\n3. Деление нацело")
    choice = input("Выберите вид деления (1-3): ")

    if choice not in {'1', '2', '3'}:
        raise ValueError("Неизвестный тип деления!")

    a = get_number("Делимое: ")
    b = get_number("Делитель: ")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Делимое и делитель должны быть числами!")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")

    if choice == '1':
        res = a / b
    elif choice == '2':
        res = a % b
    else:
        res = a // b

    return format_result(res)


def calculate_power():
    base = get_number("Основание: ")
    exponent = get_number("Показатель: ")
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise ValueError("Основание и показатель должны быть числами!")
    return format_result(base ** exponent)


def calculate_factorial():
    n = get_integer("Число: ")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Число должно быть неотрицательным целым!")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return format_result(res)


def calculate_average():
    nums_input = input("Введите числа через пробел: ").split()
    if not nums_input:
        raise ValueError("Список чисел не может быть пустым!")

    nums = []
    for num in nums_input:
        try:
            num_float = float(num)
            if not isinstance(num_float, (int, float)):
                raise ValueError("Все элементы должны быть числами!")
            nums.append(num_float)
        except ValueError:
            raise ValueError("Можно вводить только числа!")

    return format_result(sum(nums) / len(nums))


def calculate_sqrt():
    num = get_number("Число: ")
    if not isinstance(num, (int, float)):
        raise ValueError("Число должно быть числовым!")
    if num < 0:
        raise ValueError("Число должно быть неотрицательным!")
    return format_result(num ** 0.5)


OPERATIONS = {
    '1': ("Сложение", calculate_sum),
    '2': ("Вычитание", calculate_difference),
    '3': ("Умножение", calculate_product),
    '4': ("Деление", calculate_division),
    '5': ("Возведение в степень", calculate_power),
    '6': ("Факториал", calculate_factorial),
    '7': ("Среднее арифметическое", calculate_average),
    '8': ("Квадратный корень", calculate_sqrt)
}

while True:
    print("\nДоступные операции:")
    for key, (name, _) in OPERATIONS.items():
        print(f"{key}. {name}")
    print("exit - Выход")
    print("-------------------------")

    op = input("Операция: ").strip()

    if op == "exit":
        break

    try:
        if op in OPERATIONS:
            print(OPERATIONS[op][1]())
        else:
            print("Неизвестная операция!")
    except Exception as e:
        print(f"Ошибка: {e}")

    input("Нажмите Enter чтобы продолжить...")
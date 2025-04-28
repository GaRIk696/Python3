def multiply(nums: list[int], factor: int = 2) -> list[int]:
    return [x * factor for x in nums]


multiply_lambda = lambda nums, f=2: [n * f for n in nums]

def main():
    nums = []
    while not nums:
        try:
            nums = [int(n) for n in input("Введите числа через пробел: ").split()]
        except:
            print("Вводите только целые числа")

    factor = input("Введите множитель (по умолчанию 2): ")
    factor = int(factor) if factor else 2

    print("Результат (функция):", multiply(nums, factor))
    print("Результат (лямбда):", multiply_lambda(nums, factor))

main()
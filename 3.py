def function_name(search: str, status: bool, *args: object, **kwargs: object) -> list[int] | str:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search: "args" для обработки позиционных аргументов, "kwargs" для именованных
        status: влияет на формат обработки позиционных аргументов
        *args: произвольные позиционные аргументы
        **kwargs: произвольные именованные аргументы

    Возвращает:
        list[int]: если search="args" и status=True (только целые числа)
        str: если search="args" и status=False (конкатенация)
             или search="kwargs" (пары ключ-значение)

    Выбрасывает:
        ValueError: при недопустимом значении search
    """
    result: list[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += str(i)
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2.rstrip("; ")
    else:
        raise ValueError("Недопустимое значение search. Допустимо: 'args' или 'kwargs'")
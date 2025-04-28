# Аннотация типов

# Исходная функция:
def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list or str:
    """
    Создается функция function_name с параметрами
    :param search: с аннотацией типа str - определяет режим работы либо с args, либо с kwargs
    :param status: с аннотацией типа bool - флаг для обработки args true или false
    :param args: с аннотацией типа tuple - позиционные аргументы, которые попадают в функцию как кортеж
    :param kwargs: с аннотацией типа dict именованные аргументы, которые попадают в функцию как словарь
    :return: написана аннотация для возвращаемого значения -> list or str которые записаны в result и result_2

    Для search="args" и status=True возвращает список целых чисел из args
    Для search="args" и status=False возвращает строку из всех args
    Для search="kwargs" возвращает строку с представлением всех kwargs, перебирает каждый ключ и значение из словаря

    также есть исключение ValueError если передан недопустимый параметр search
    """
    result: list = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
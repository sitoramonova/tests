from functools import wraps
from typing import get_type_hints


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов функции
        type_hints = get_type_hints(func)

        # Проверяем только позиционные аргументы (kwargs исключены)
        for arg_value, (arg_name, expected_type) in zip(args, type_hints.items()):
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(arg_value).__name__}"
                )

        return func(*args, **kwargs)

    return wrapper

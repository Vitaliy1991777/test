def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов
        annotations = func.__annotations__
        
        # Проверка позиционных аргументов
        for arg_name, arg_value in zip(annotations.keys(), args):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Argument '{arg_name}' must be of type {expected_type}, but got {type(arg_value)}")
        
        # Проверка именованных аргументов
        for arg_name, arg_value in kwargs.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(f"Argument '{arg_name}' must be of type {expected_type}, but got {type(arg_value)}")
        
        # Вызов оригинальной функции
        return func(*args, **kwargs)
    
    return wrapper

# Тестирование декоратора
@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# Пример работы
print(sum_two(1, 2))   # >>> 3
try:
    print(sum_two(1, 2.4))  # >>> TypeError
except TypeError as e:
    print(e)


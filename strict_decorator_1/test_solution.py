# Импортируем функцию sum_two из основного файла
from solution import sum_two

def test_strict_decorator():
    # Тестируем правильную работу
    assert sum_two(1, 2) == 3, "Expected sum_two(1, 2) to return 3"

    # Тест на выброс исключения TypeError при неправильном типе второго аргумента
    try:
        sum_two(1, 2.4)  # должен выбросить TypeError
    except TypeError:
        pass  # Ожидаем исключение, тест прошел
    else:
        assert False, "Expected TypeError but no exception was raised"

    # Тест на выброс исключения TypeError при неправильных типах аргументов
    try:
        sum_two("1", "2")  # должен выбросить TypeError
    except TypeError:
        pass  # Ожидаем исключение, тест прошел
    else:
        assert False, "Expected TypeError but no exception was raised"

    print("All tests passed successfully!")

# Запуск тестов
test_strict_decorator()

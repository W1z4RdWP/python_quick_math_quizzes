import time
from typing import Callable


def timer_with_parameter(is_countdown: int, seconds: int = 0) -> Callable:
    """

    :param is_countdown: 0 - если хотим использовать как секундомер, 1 - если используем как таймер.
    Таймер - задается количество секунд, после которого выполнение функции завершается.
    :param seconds: Количество секунд после которого выполнение обернутой функции завершается, для таймера
    :return: Callable
    """
    def timer(func):
        def wrapper(*args, **kwargs):
            if is_countdown:
                start_time = time.time()
                while time.time() - start_time < seconds:
                    func(*args, **kwargs)
                end_time = time.time()
                res_time = end_time - start_time
            else:
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                res_time = end_time - start_time
            print("Прошло времени: ", round(res_time,2), "секунд")
            return round(res_time,2)
        return wrapper
    return timer


if __name__ == "__main__":
    """
    Локальное тестирование utils кода
    """
    @timer_with_parameter(1, 6)
    def my_func():
        count = 0
        print("Hi!")


    my_func()
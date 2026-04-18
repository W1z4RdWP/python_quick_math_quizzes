import time
import threading
from functools import wraps
from typing import Callable


def timer_with_parameter(is_countdown: int = 0, seconds: int = 0) -> Callable:
    """
    Таймер с параметрами

    :param is_countdown: 0 - если хотим использовать как секундомер, 1 - если используем как таймер; Если используется как Таймер - задается количество секунд, после которого выполнение функции завершается.
    :param seconds: Количество секунд после которого выполнение обернутой функции завершается, для таймера
    :return: Callable
    """
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_countdown and seconds > 0:
                result = [None]
                exception = [None]

                def target():
                    try:
                        result[0] = func(*args, **kwargs)
                    except Exception as e:
                        exception[0] = e

                thread = threading.Thread(target=target)
                thread.daemon = True
                thread.start()
                thread.join(seconds)

                if thread.is_alive():
                    print("Время вышло!")
                    return
                if exception[0]:
                    raise exception[0]
                return result[0]
            else:
                start = time.time()
                res = func(*args, **kwargs)
                print(f"Прошло времени: {round(time.time() - start, 2)} сек.")
                return res
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
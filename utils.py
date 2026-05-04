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
                stats=[None]

                def target():
                    try:
                        result[0] = func(*args, **kwargs)

                        # После выполнения функции забираем статистику из объекта
                        if args and hasattr(args[0], '_correct_answers'):
                            obj = args[0]
                            correct = getattr(obj, '_correct_answers', 0)
                            incorrect = getattr(obj, '_incorrect_answers', 0)
                            stats[0] = (correct, correct+incorrect)
                    except Exception as e:
                        exception[0] = e

                thread = threading  .Thread(target=target)
                thread.daemon = True
                thread.start()
                thread.join(seconds)

                if thread.is_alive():
                    print("Время вышло!")
                    if stats[0]:
                        correct, total = stats[0]
                        print(f"Правильных ответов: {correct}/{total}")
                    elif args and hasattr(args[0], '_correct_answers'):
                        obj = args[0]
                        correct = getattr(obj, '_correct_answers', 0)
                        incorrect = getattr(obj, '_incorrect_answers', 0)
                        print(f"Правильных ответов: {correct}/{correct+incorrect}")
                    else:
                        print("Без результата")
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
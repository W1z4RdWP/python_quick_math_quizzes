import time, random
from typing import Callable

from utils import timer_with_parameter


class Quiz:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self._questions_amount = 10
        self._correct_answers = 0
        self._current_question = 0
        self._correct_answers = 0
        self._incorrect_answers = 0
        self._last_answer = 0

    def start_quiz(self):
        # Легкая сложность
        if self.difficulty == 0:
            print("Выбери тип теста")

        # Средняя сложность
        if self.difficulty == 1:
            print("Выбери тип теста")



class MultiplicationQuiz(Quiz):
    @timer_with_parameter(0)
    def multiplication_quiz(self, base_num: int, end_num: int) -> None:
        while self._current_question < self._questions_amount:
            self._current_question += 1
            num_1 = random.randint(base_num, end_num)
            num_2 = random.randint(base_num, end_num)
            question = input(f"Сколько будет {num_1} * {num_2}?: ")
            if question == 'stop':
                print(f"Прерываем. Твой результат: {self._correct_answers}/{self._incorrect_answers + self._correct_answers}")
                break
            if int(question) == num_1 * num_2:
                self._correct_answers += 1
                print("Поздравляю! Ответ правильный!")
            else:
                self._incorrect_answers += 1
                print(f"Увы :(. \nТвой ответ:{question}\nПравильный ответ: {num_1 * num_2}")
        print(
            f"Правильных ответов: {self._correct_answers}/{self._incorrect_answers + self._correct_answers}")

    def start_quiz(self)->None:
        """
            Метод для проверки навыков умножения двух чисел
        :return: None
        """
        if self.difficulty == 0:
            self.multiplication_quiz(1, 12)
        elif self.difficulty == 1:
            self.multiplication_quiz(10, 50)
        elif self.difficulty == 2:
            self.multiplication_quiz(40, 100)
        else:
            print("Incorrect difficulty set")




class SummaryQuiz(Quiz):
    @timer_with_parameter(0)
    def summary_quiz(self, base_num: int, end_num:int) -> None:
        while self._current_question < self._questions_amount:
            self._current_question += 1
            num_1 = random.randint(base_num, end_num)
            num_2 = random.randint(base_num, end_num)
            question = int(input(f"Сколько будет {num_1} + {num_2}?: "))
            if question == num_1 + num_2:
                self._correct_answers += 1
                print("Поздравляю! Ответ правильный!")
            else:
                self._incorrect_answers += 1
                print(f"Увы :(. \nТвой ответ:{question}\nПравильный ответ: {num_1 + num_2}")
        print(
            f"Правильных ответов: {self._correct_answers}/{self._incorrect_answers + self._correct_answers}")

    def start_quiz(self) -> None:
        # Легкая сложность
        if self.difficulty == 0:
            self.summary_quiz(1,100)

        # Средняя сложность
        if self.difficulty == 1:
            self.summary_quiz(45,300)

        # Сложная сложность
        if self.difficulty == 2:
            self.summary_quiz(100, 1000)


class SequentialArithmeticQuiz(Quiz):

    @timer_with_parameter(1,10)
    def sequential_quiz(self, base_num: int, end_num: int) -> None:
        num_1 = random.randint(base_num, end_num)

        while True:
            num_2 = random.randint(base_num, end_num)

            try:
                answer = int(input(f"{num_1} + {num_2} = "))
            except ValueError:
                answer = 0 # Если введено не число, то считаем ответ не верным и продолжаем

            # Проверка правильности
            if answer == (num_1+num_2):
                self._correct_answers += 1
            else:
                self._incorrect_answers += 1

            self._last_answer = answer
            num_1 = answer


    def __del__(self):
        """Вывод статистики при удалении объекта."""
        total = self._correct_answers + self._incorrect_answers
        if total > 0:
            print(f"Правильных ответов: {self._correct_answers}/{total}")
        else:
            print("Правильных ответов 0/0")


    def start_quiz(self) -> None:
        if self.difficulty == 0:
            self.sequential_quiz(1,100)
        elif self.difficulty == 1:
            self.sequential_quiz(50, 300)
        elif self.difficulty == 2:
            self.sequential_quiz(100, 500)



if __name__ == "__main__":
    summary_choices = ["сложение", "1", 1]
    multiplication_choices = ["умножение", "2", 2]
    sequential_choices = ["последовательность", "3", 3]
    quiz_type = input("Что выбираешь?:\n1) Сложение\n2) Умножение\n3) Последовательность")
    difficulty_choice = int(input("Выбери сложность от 0 до 2: "))
    if quiz_type.lower() in summary_choices:
        quiz = SummaryQuiz(difficulty_choice)
        quiz.start_quiz()
    elif quiz_type.lower() in multiplication_choices:
        quiz = MultiplicationQuiz(difficulty_choice)
        quiz.start_quiz()
    elif quiz_type.lower() in sequential_choices:
        quiz = SequentialArithmeticQuiz(difficulty_choice)
        quiz.start_quiz()
    else:
        print("Заданы неизвестные параметры")

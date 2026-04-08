import time, random


class Quiz:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.questions_amount = 0
        self.correct_answers = 0
        self.current_question = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def get_quiz(self):
        # Легкая сложность
        if self.difficulty == 0:
            print("Выбери тип теста")

        # Средняя сложность
        if self.difficulty == 1:
            print("Выбери тип теста")



class MultiplicationQuiz(Quiz):
    def multiplication_quiz(self, base_num, end_num):
        self.questions_amount = 10
        start_time = time.time()
        while self.current_question < self.questions_amount:
            self.current_question += 1
            num_1 = random.randint(base_num, end_num)
            num_2 = random.randint(base_num, end_num)
            question = int(input(f"Сколько будет {num_1} * {num_2}?: "))
            if question == num_1 * num_2:
                self.correct_answers += 1
                print("Поздравляю! Ответ правильный!")
            else:
                self.incorrect_answers += 1
                print(f"Увы :(. \nТвой ответ:{question}\nПравильный ответ: {num_1 * num_2}")
        end_time = time.time()
        res_time = end_time - start_time
        print(
            f"Правильных ответов: {self.correct_answers}/{self.incorrect_answers + self.correct_answers}\nЗаняло времени: {round(res_time, 2)} секунд.")

    def get_quiz(self):
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
    def summary_quiz(self, base_num, end_num):
        self.questions_amount = 10
        start_time = time.time()
        while self.current_question < self.questions_amount:
            self.current_question += 1
            num_1 = random.randint(base_num, end_num)
            num_2 = random.randint(base_num, end_num)
            question = int(input(f"Сколько будет {num_1} + {num_2}?: "))
            if question == num_1 + num_2:
                self.correct_answers += 1
                print("Поздравляю! Ответ правильный!")
            else:
                self.incorrect_answers += 1
                print(f"Увы :(. \nТвой ответ:{question}\nПравильный ответ: {num_1 + num_2}")
        end_time = time.time()
        res_time = end_time - start_time
        print(
            f"Правильных ответов: {self.correct_answers}/{self.incorrect_answers + self.correct_answers}\nЗаняло времени: {round(res_time, 2)} секунд.")

    def get_quiz(self):
        # Легкая сложность
        if self.difficulty == 0:
            self.summary_quiz(1,100)

        # Средняя сложность
        if self.difficulty == 1:
            self.summary_quiz(45,300)

        # Сложная сложность
        if self.difficulty == 2:
            self.summary_quiz(100, 1000)



if __name__ == "__main__":
    summary_choices = ["сложение", "1", 1]
    multiplication_choices = ["умножение", "2", 2]
    quiz_type = input("Что выбираешь?:\n1) Сложение\n2) Умножение")
    difficulty_choice = int(input("Выбери сложность от 0 до 2: "))
    if quiz_type.lower() in summary_choices:
        quiz = SummaryQuiz(difficulty_choice)
        quiz.get_quiz()
    elif quiz_type.lower() in multiplication_choices:
        quiz = MultiplicationQuiz(difficulty_choice)
        quiz.get_quiz()
    else:
        print("Заданы неизвестные параметры")

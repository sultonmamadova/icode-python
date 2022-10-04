import random


class DB:

    questions = [
        {
            "question": "Зимой и летом одним цветом",
            "answers": [
                {
                    "text": "Елка",
                    "correct": True
                },
                {
                    "text": "Дерево",
                    "correct": False
                },
                {
                    "text": "Дом",
                    "correct": False
                },
                {
                    "text": "Птица",
                    "correct": False
                },
            ]
        },
        {
            "question": "Без рук и ног, а в дом не пускает",
            "answers": [
                {
                    "text": "Дверь",
                    "correct": True
                },
                {
                    "text": "Ключ",
                    "correct": False
                },
                {
                    "text": "Огород",
                    "correct": False
                },
                {
                    "text": "Машина",
                    "correct": False
                },
            ]
        }
    ]

    answers = {
        "correct": [],
        "uncorrect": [],
    }

    def get_question(self):
        return random.choice(self.questions)

    def update_answers(self, question, answer, is_correct):
        data = {
            "question": question["question"],
            "answer": question["answers"][answer]["text"]
        }

        if is_correct:
            self.answers["correct"].append(data)
        else:
            self.answers["uncorrect"].append(data)

class BL:

    def check_answer(self, question, answer):
        try:
            return question["answers"][answer]["correct"]
        except IndexError:
            return False


class UI:

    def show_question(self, question, per_line=False):
        self.show_question_text(question=question)
        
        print("Варианты ответов:")
        
        if per_line:
            self.show_answers_per_line(question["answers"])
        else:
            self.show_answers_columed(question["answers"])
        
        print()

    def show_question_text(self, question):
        print()
        print("Вам достался вопрос:", end="\n\n")
        print(question["question"], end="\n\n")

    def ask_input(self):
        answer = input("Ваш выбор: \n")
        return int(answer) - 1

    def show_correct_response(self):
        print()
        print("Ура. Вы выбрали правильный вариант.", end="\n\n")
    
    def show_uncorrect_response(self):
        print()
        print("Упс. Неверный вариант", end="\n\n")

    def show_answers_per_line(self, answers): 
        for idx, answer in enumerate(answers):
            print(f"{idx + 1}. {answer['text']}")

    def show_answers_columed(self, answers):
        max_len = max(len(x["text"]) for x in answers)
        line_text = ""
        for idx, answer in enumerate(answers):
            line_text += f"{idx + 1}. {answer['text']}{self.get_gap(answer['text'], max_len)}"

            if idx % 2 == 1:
                print(line_text)
                line_text = ""
        
    def get_gap(self, word, max_len, default_gap=2):
        return " " * (max_len - len(word) + default_gap)

    def show_result(self, data):
        print()
        print("Правильные ответы:")

        for item in data["correct"]:
            print(item["question"])
            print(item["answer"])
            print()

        print("Неправильные ответы:")
        
        for item in data["correct"]:
            print(item["question"])
            print(item["answer"])
            print()

class App:

    def run(self):
        db = DB()
        ui = UI()
        bl = BL()
        question = db.get_question()

        ui.show_question(question)
        answer = ui.ask_input()

        is_correct = bl.check_answer(question, answer)

        if is_correct:
            ui.show_correct_response()
        else:
            ui.show_uncorrect_response()
    
    def run_loop(self):
        db = DB()
        ui = UI()
        bl = BL()

        stop = 0
        while stop < len(db.questions):
            question = db.get_question()
            ui.show_question(question)
            answer = ui.ask_input()
            
            is_correct = bl.check_answer(question, answer)

            if is_correct:
                db.update_answers(question=question, answer=answer, is_correct=is_correct)
            else:
                db.update_answers(question=question, answer=answer, is_correct=is_correct)

            stop += 1

        ui.show_result(data=db.answers)

def main():
    app = App()
    app.run()
    # app.run_loop()


if __name__ == "__main__":
    main()

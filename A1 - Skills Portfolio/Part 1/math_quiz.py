import tkinter as tk
import random

# microsoft copilot was used for general structure conception but mostly for error debugging assistance, prompts asked would mention terminal error messages
# most of the code was cross referenced with sololearn python course, great learning course and advanced programming lesson slides

class MathQuizProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("800x800")

        self.difficulty = None
        self.score = 0
        self.question_number = 0
        self.total_questions = 10
        self.current_answer = 0
        self.is_retry = False

        self.difficulty_ranges = {
            1: (1, 9),
            2: (10, 99),
            3: (100, 999)
        }

        self.setup_frames()
        self.display_menu()

    def setup_frames(self):
        # menu frame
        self.menu_frame = tk.Frame(self.root)
        tk.Label(self.menu_frame, text="Pick a difficulty for your Math Quiz", font=("Times New Roman", 20)).pack(pady=20)
        tk.Button(self.menu_frame, text="Easy", font=("Times New Roman", 16), width=20,
                  command=lambda: self.start_quiz(1)).pack(pady=10)
        tk.Button(self.menu_frame, text="Moderate", font=("Times New Roman", 16), width=20,
                  command=lambda: self.start_quiz(2)).pack(pady=10)
        tk.Button(self.menu_frame, text="Advanced", font=("Times New Roman", 16), width=20,
                  command=lambda: self.start_quiz(3)).pack(pady=10)
        self.root.bind("<Return>", lambda event: self.submit_answer()) #Makes it easier to enter answers

        # quiz frame
        self.quiz_frame = tk.Frame(self.root)
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Times New Roman", 18))
        self.question_label.pack(pady=20)
        self.answer_entry = tk.Entry(self.quiz_frame, font=("Times New Roman", 18))
        self.answer_entry.pack(pady=10)
        self.submit_btn = tk.Button(self.quiz_frame, text="Submit", font=("Times New Roman", 16),
                                    command=self.submit_answer)
        self.submit_btn.pack(pady=10)
        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Times New Roman", 14))
        self.feedback_label.pack(pady=10)

        # result frame
        self.result_frame = tk.Frame(self.root)
        self.result_label = tk.Label(self.result_frame, text="", font=("Times New Roman", 20))
        self.result_label.pack(pady=20)
        tk.Button(self.result_frame, text="Play Again", font=("Times New Roman", 16),
                  command=self.display_menu).pack(pady=10)
        tk.Button(self.result_frame, text="Exit", font=("Times New Roman", 16),
                  command=self.root.quit).pack(pady=10)

    def display_menu(self):
        self.menu_frame.pack()
        self.quiz_frame.pack_forget()
        self.result_frame.pack_forget()

    def start_quiz(self, level):
        self.difficulty = level
        self.score = 0
        self.question_number = 0
        self.is_retry = False
        self.menu_frame.pack_forget()
        self.result_frame.pack_forget()
        self.quiz_frame.pack()
        self.display_problem()

    def random_int(self):
        low, high = self.difficulty_ranges[self.difficulty]
        return random.randint(low, high)

    def decide_operation(self):
        return random.choice(['+', '-'])

    def is_correct(self, user_ans):
        try:
            return int(user_ans) == self.current_answer
        except ValueError:
            return False

    def display_problem(self):
        if self.question_number >= self.total_questions:
            self.display_results()
            return

        num1 = self.random_int()
        num2 = self.random_int()
        op = self.decide_operation()

        self.current_answer = num1 + num2 if op == '+' else num1 - num2
        self.question_label.config(text=f"Question {self.question_number + 1}: {num1} {op} {num2} = ")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.submit_btn.config(state="normal")
        self.is_retry = False
        self.question_number += 1

    def submit_answer(self):
        user_input = self.answer_entry.get()
        if user_input.strip() == "":
            self.feedback_label.config(text="Please enter an answer.")
            return

        self.submit_btn.config(state="disabled")

        if self.is_correct(user_input):
            if self.is_retry:
                self.feedback_label.config(text="Correct on retry!", fg="blue")
                self.score += 5
            else:
                self.feedback_label.config(text="Correct!", fg="green")
                self.score += 10
            self.is_retry = False
            self.root.after(1000, self.display_problem)
        else:
            if self.is_retry:
                self.feedback_label.config(text=f"Incorrect again! The correct answer was {self.current_answer}", fg="red")
                self.is_retry = False
                self.root.after(1000, self.display_problem)
            else:
                self.feedback_label.config(text="Incorrect! Try again.", fg="orange")
                self.is_retry = True
                self.submit_btn.config(state="normal")

    def display_results(self):
        self.quiz_frame.pack_forget()
        self.result_label.config(text=f"Your score: {self.score}/100")
        self.result_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizProgram(root)
    root.mainloop()
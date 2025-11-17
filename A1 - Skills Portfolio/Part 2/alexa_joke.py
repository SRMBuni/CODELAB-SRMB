import tkinter as tk
import random
from pathlib import Path

# program was assisted by microsoft copilot but mostly regarding error corrections, prompts asked would mention terminal error messages
# programming concepts are crossreferenced with sololearn python course, great learning tkinter course and advanced programming lesson slides

class AlexaJokester:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa the Jester")
        self.root.geometry("650x450")

        # asked copilot how to properly path the text file code below is mostly assisted
        script_dir = Path(r"C:\Users\rayne\OneDrive\Documents\GitHub\CODELAB-2--A1\A1 - Skills Portfolio\Part 2")
        joke_file = script_dir / "randomJokes.txt"
        #until here

        self.jokes = []
        try:
            with open(joke_file, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if "?" in line:
                        setup, punchline = line.split("?", 1)
                        self.jokes.append((setup + "?", punchline.strip()))
        except FileNotFoundError:
            self.jokes = ["Joke file not found :("]
            
        self.current_punchline = ""

# all GUI Below

        self.prompt_label = tk.Label(root, text="Type your command:", font=("Times New Roman", 16))
        self.prompt_label.pack(pady=10)

        self.command_entry = tk.Entry(root, font=("Times New Roman", 16), width=40)
        self.command_entry.pack(pady=10)
        self.command_entry.bind("<Return>", self.check_command)

        self.joke_label = tk.Label(root, text="", wraplength=500, font=("Times New Roman", 16), fg="blue")
        self.joke_label.pack(pady=20)

        self.punchline_btn = tk.Button(root, text="Show Punchline", font=("Times New Roman", 14), command=self.show_punchline, state="disabled")
        self.punchline_btn.pack()

        self.submit_btn = tk.Button(root, text="Show a joke", font=("Times New Roman", 14), command=self.check_command)
        self.submit_btn.pack(pady=10)

    def check_command(self, event=None):
        user_input = self.command_entry.get().strip().lower()
        if user_input == "alexa tell me a joke":
            setup, punchline = random.choice(self.jokes)
            self.joke_label.config(text=setup)
            self.current_punchline = punchline
            self.punchline_btn.config(state="normal")
        else:
            self.joke_label.config(text="Try saying: Alexa tell me a joke")
            self.punchline_btn.config(state="disabled")

    def show_punchline(self):
        self.joke_label.config(text=self.joke_label.cget("text") + "\n\n" + self.current_punchline)
        self.punchline_btn.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlexaJokester(root)
    root.mainloop()
import tkinter as tk
from tkinter import font
from data import LOCALIZATION_STRINGS, QUIZ_TOPICS, quiz_questions

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Quiz")
        self.geometry("500x700")
        self.language = "english"  # Default language
        self.current_question_index = 0
        self.total_score = 0
        self.selected_quiz_topic = "quiz_culture"  # Default quiz topic

        # Create a master frame to hold pages
        self.master_frame = tk.Frame(self)
        self.master_frame.pack(fill="both", expand=True)

        # Create frames for each page
        self.start_page_frame = tk.Frame(self.master_frame)
        self.language_page_frame = tk.Frame(self.master_frame)
        self.about_this_game_page_frame = tk.Frame(self.master_frame)
        self.quiz_selection_page_frame = tk.Frame(self.master_frame)
        self.quiz_page_frame = tk.Frame(self.master_frame)

        # Setup pages
        self.setup_start_page()
        self.setup_language_page()
        self.setup_about_this_game_page()
        self.setup_quiz_selection_page()

        # Initially show the start page
        self.show_start_page()

        self.update_fonts()  # Adjust fonts based on window size

        # Bind resizing event
        self.bind("<Configure>", self.on_resize)

    def update_fonts(self):
        base_font = font.nametofont("TkDefaultFont")
        base_font_size = max(10, int(self.winfo_height() / 50))
        base_font.configure(size=base_font_size)

    def on_resize(self, event):
        self.update_fonts()

    def show_start_page(self):
        self.start_page_frame.pack(fill="both", expand=True)
        self.language_page_frame.pack_forget()
        self.about_this_game_page_frame.pack_forget()
        self.quiz_selection_page_frame.pack_forget()
        self.quiz_page_frame.pack_forget()

    def show_language_page(self):
        self.language_page_frame.pack(fill="both", expand=True)
        self.start_page_frame.pack_forget()
        self.about_this_game_page_frame.pack_forget()
        self.quiz_selection_page_frame.pack_forget()
        self.quiz_page_frame.pack_forget()

    def show_about_this_game_page(self):
        self.about_this_game_page_frame.pack(fill="both", expand=True)
        self.start_page_frame.pack_forget()
        self.language_page_frame.pack_forget()
        self.quiz_selection_page_frame.pack_forget()
        self.quiz_page_frame.pack_forget()

    def show_quiz_selection_page(self, language):
        self.language = language
        self.quiz_selection_page_frame.pack(fill="both", expand=True)
        self.start_page_frame.pack_forget()
        self.language_page_frame.pack_forget()
        self.about_this_game_page_frame.pack_forget()
        self.quiz_page_frame.pack_forget()

    def show_quiz_page(self):
        self.quiz_page_frame.pack(fill="both", expand=True)
        self.start_page_frame.pack_forget()
        self.language_page_frame.pack_forget()
        self.about_this_game_page_frame.pack_forget()
        self.quiz_selection_page_frame.pack_forget()

        # Initialize score label
        if not hasattr(self, 'label_score'):
            self.label_score = tk.Label(self.quiz_page_frame, text=f"Score: {self.total_score}/{self.current_question_index}")
            self.label_score.pack(pady=10)

    def start_quiz(self, quiz_topic):
        self.selected_quiz_topic = quiz_topic
        self.current_question_index = 0
        self.total_score = 0
        self.show_quiz_page()
        self.show_next_question()

    def show_next_question(self):
        if self.current_question_index < len(quiz_questions[self.language][self.selected_quiz_topic]):
            question = quiz_questions[self.language][self.selected_quiz_topic][self.current_question_index]

            # Clear the quiz page frame
            for widget in self.quiz_page_frame.winfo_children():
                widget.destroy()

            self.label_quiz_question = tk.Label(self.quiz_page_frame, text=question['question'])
            self.label_quiz_question.pack(pady=20)

            self.buttons = []
            for idx, option in enumerate(question['options']):
                btn = tk.Button(self.quiz_page_frame, text=option, command=lambda opt=option: self.select_answer(opt))
                btn.pack(anchor="w", pady=5)
                self.buttons.append(btn)
        else:
            self.show_final_score()

    def select_answer(self, selected_option):
        self.selected_answer = selected_option
        self.check_answer()

    def check_answer(self):
        question = quiz_questions[self.language][self.selected_quiz_topic][self.current_question_index]
        correct_answer = question['correct_answer']

        # Disable all buttons to prevent further interaction
        for btn in self.buttons:
            btn.configure(state=tk.DISABLED)

        # Highlight correct and incorrect answers
        for idx, option in enumerate(question['options']):
            if option == correct_answer:
                self.buttons[idx].configure(bg="green")
            elif option == self.selected_answer:
                self.buttons[idx].configure(bg="red")

        # Check selected answer against correct answer
        if self.selected_answer == correct_answer:
            self.total_score += 1
            score_feedback = "Correct!"
        else:
            score_feedback = f"Incorrect. Correct answer: {correct_answer}"

        # Display score feedback
        self.label_score_feedback = tk.Label(self.quiz_page_frame, text=score_feedback)
        self.label_score_feedback.pack(pady=10)

        # Update score display
        self.label_score.config(text=f"Score: {self.total_score}/{self.current_question_index + 1}")

        # Move to the next question after a delay
        self.current_question_index += 1
        if self.current_question_index < len(quiz_questions[self.language][self.selected_quiz_topic]):
            self.after(2000, self.show_next_question)
        else:
            self.after(2000, self.show_final_score)

    def show_final_score(self):
        for widget in self.quiz_page_frame.winfo_children():
            widget.destroy()

        score_text = f"Your total score is {self.total_score}/{len(quiz_questions[self.language][self.selected_quiz_topic])}"
        self.label_final_score = tk.Label(self.quiz_page_frame, text=score_text)
        self.label_final_score.pack(pady=20)

        self.button_go_back_to_start = tk.Button(self.quiz_page_frame, text="Go Back to Start", command=self.show_start_page)
        self.button_go_back_to_start.pack(pady=20)

    def exit_game(self):
        self.destroy()

    def setup_start_page(self):
        self.label_start = tk.Label(self.start_page_frame, text="Welcome to the Quiz!")
        self.label_start.pack(pady=20)

        self.button_play = tk.Button(
            self.start_page_frame,
            text="Play Game",
            command=self.show_language_page
        )
        self.button_play.pack(pady=20)

        self.button_about_this_game = tk.Button(
            self.start_page_frame,
            text="How to play",
            command=self.show_about_this_game_page
        )
        self.button_about_this_game.pack(pady=20)

        self.button_exit = tk.Button(
            self.start_page_frame,
            text="Exit Game",
            command=self.exit_game
        )
        self.button_exit.pack(pady=20)

    def setup_language_page(self):
        self.label_language = tk.Label(self.language_page_frame, text="Please select a language you comfortably understand")
        self.label_language.pack(pady=20)

        self.button_english_quiz = tk.Button(
            self.language_page_frame,
            text="English",
            command=lambda: self.show_quiz_selection_page('english')
        )
        self.button_english_quiz.pack(pady=20)

        self.button_japanese_quiz = tk.Button(
            self.language_page_frame,
            text="Japanese",
            command=lambda: self.show_quiz_selection_page('japanese')
        )
        self.button_japanese_quiz.pack(pady=20)

    def setup_about_this_game_page(self):
        self.label_about_this_game = tk.Label(
            self.about_this_game_page_frame,
            text=LOCALIZATION_STRINGS['quiz_info'].get(self.language, "Information not available")
        )
        self.label_about_this_game.pack(pady=20)

        self.button_go_back_to_start = tk.Button(
            self.about_this_game_page_frame,
            text="Go Back",
            command=self.show_start_page
        )
        self.button_go_back_to_start.pack(pady=20)

    def setup_quiz_selection_page(self):
        self.label_select_quiz = tk.Label(self.quiz_selection_page_frame, text="Please select a quiz topic")
        self.label_select_quiz.pack(pady=20)

        self.button_culture_quiz = tk.Button(
            self.quiz_selection_page_frame,
            text="Culture",
            command=lambda: self.start_quiz('quiz_culture')
        )
        self.button_culture_quiz.pack(pady=20)

        self.button_geography_quiz = tk.Button(
            self.quiz_selection_page_frame,
            text="Geography",
            command=lambda: self.start_quiz('quiz_geography')
        )
        self.button_geography_quiz.pack(pady=20)

        self.button_foods_quiz = tk.Button(
            self.quiz_selection_page_frame,
            text="Foods",
            command=lambda: self.start_quiz('quiz_foods')
        )
        self.button_foods_quiz.pack(pady=20)

        self.button_go_back = tk.Button(
            self.quiz_selection_page_frame,
            text="Go Back",
            command=self.show_language_page
        )
        self.button_go_back.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()

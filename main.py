import tkinter as tk  # Import the tkinter library for creating the GUI
from tkinter import font  # Import the font module from tkinter for font customization
from data import LOCALIZATION_STRINGS, QUIZ_TOPICS, quiz_questions, quiz_feedback # Import data from the 'data' module
# - LOCALIZATION_STRINGS: A dictionary containing localized strings for different languages
# - QUIZ_TOPICS: A dictionary mapping quiz topic keys to their display names
# - quiz_questions: A nested dictionary containing quiz questions in different languages and topics
# - quiz_feedback: A nested dictionary containing feedback for correct and incorrect answers

class App(tk.Tk):
    def __init__(self):
        """
        Initializes the main application window.

        This function sets up the basic structure of the application, including
        the title, geometry, default language, initial question index, total
        score, selected quiz topic, and frames for different pages.
        """
        super().__init__()
        self.title("My Quiz")
        self.geometry("1100x900")
        self.language = "english"  # Default language
        self.current_question_index = 0
        self.total_score = 0
        self.selected_quiz_topic = "quiz_culture"  # Default quiz topic

        # Create a master frame to hold pages
        self.master_frame = tk.Frame(self)
        self.master_frame.pack(fill="both", expand=True)

        # Create frames for each page
        self.frames = {}
        for page in ("start", "language", "about", "quiz_selection", "quiz", "final_score"):
            frame = tk.Frame(self.master_frame)
            self.frames[page] = frame

        # Setup pages
        self.setup_start_page()
        self.setup_language_page()
        self.setup_about_this_game_page()
        self.setup_quiz_selection_page()

        # Initially show the start page
        self.show_page("start")

        self.update_fonts()  # Adjust fonts based on window size

        # Bind resizing event
        self.bind("<Configure>", self.on_resize)

    def update_fonts(self):
        """
        Adjusts the fonts based on the window size.

        This function ensures that the font size scales appropriately based
        on the height of the window, making the text legible at different
        window sizes.
        """
        base_font = font.nametofont("TkDefaultFont")
        base_font_size = max(10, int(self.winfo_height() / 50))
        base_font.configure(size=base_font_size)

    def on_resize(self, event):
        """
        Updates the fonts when the window is resized.

        This function is called whenever the window is resized, and it
        re-adjusts the font sizes to maintain readability.
        """
        self.update_fonts()

    def show_page(self, page_name):
        """
        Shows the specified page by packing it and hiding others.

        This function takes a page name as input and makes that page visible
        while hiding all other pages.
        """
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[page_name].pack(fill="both", expand=True)

    def show_start_page(self):
        """Shows the start page."""
        self.show_page("start")

    def show_language_page(self):
        """Shows the language selection page."""
        self.show_page("language")

    def show_about_this_game_page(self):
        """Shows the about this game page."""
        self.show_page("about")
        self.update_about_page_text()

    def show_quiz_selection_page(self, language):
        """
        Shows the quiz selection page, setting the language.

        This function sets the language for the quiz and then displays the
        quiz selection page.
        """
        self.language = language
        self.show_page("quiz_selection")

    def show_quiz_page(self):
        """Shows the quiz page and displays the next question."""
        self.show_page("quiz")
        self.show_next_question()

    def start_quiz(self, quiz_topic):
        """
        Starts the quiz, resetting score and question index.

        This function sets the selected quiz topic, resets the score and
        current question index, and then displays the first question.
        """
        self.selected_quiz_topic = quiz_topic
        self.current_question_index = 0
        self.total_score = 0
        self.show_quiz_page()

    def show_next_question(self):
        """
        Displays the next question in the quiz.

        This function fetches the next question based on the current question
        index and language. It then clears the previous question's content
        and displays the new question, options, and score information.
        """
        if self.current_question_index < len(quiz_questions[self.language][self.selected_quiz_topic]):
            question = quiz_questions[self.language][self.selected_quiz_topic][self.current_question_index]

            # Clear the quiz page frame
            for widget in self.frames["quiz"].winfo_children():
                widget.destroy()

            # Add question progress label
            question_progress = f"Question {self.current_question_index + 1} of {len(quiz_questions[self.language][self.selected_quiz_topic])}"
            self.label_question_progress = tk.Label(self.frames["quiz"], text=question_progress)
            self.label_question_progress.pack(pady=10)

            self.label_quiz_question = tk.Label(self.frames["quiz"], text=question['question'])
            self.label_quiz_question.pack(pady=20)

            self.buttons = []
            for idx, option in enumerate(question['options']):
                btn = tk.Button(self.frames["quiz"], text=option, command=lambda opt=option: self.select_answer(opt))
                btn.pack(anchor="w", pady=5)
                self.buttons.append(btn)

            self.label_score = tk.Label(self.frames["quiz"], text=f"Score: {self.total_score}/{self.current_question_index}")
            self.label_score.pack(pady=10)
        else:
            self.show_final_score()

    def select_answer(self, selected_option):
        """
        Records the selected answer and checks it.

        This function stores the user's selected answer and then calls the
        check_answer function to evaluate the choice.
        """
        self.selected_answer = selected_option
        self.check_answer()

    def check_answer(self):
        """
        Checks the selected answer against the correct answer.

        This function determines if the user's answer is correct and provides
        feedback. It also updates the score and moves to the next question
        or displays the final score after a delay.
        """
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
            if self.language == 'japanese':
                score_feedback = "正解！"
            if self.selected_quiz_topic == 'quiz_culture':
                if question['question'] == 'What is the national bird of New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_bird']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_bird']}"

                elif question['question'] == 'What is the traditional Māori greeting?':
                    if self.language == 'english':
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_greeting']}"
                    else:
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_greeting']}"

                elif question['question'] == 'What is the name of the traditional Māori dance?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_traditional_dance']}"
                    else:
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_traditional_dance']}"

                elif question['question'] == 'What is the name of the traditional Māori meeting house?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_house']}"
                    else:
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_house']}"

                elif question['question'] == 'What is the name of the traditional Māori carving style?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_carving']}"
                    else:
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['correct_carving']}"


            #Feedback for the correct answers for Geography quiz
            elif self.selected_quiz_topic == 'quiz_geography':
                if question['question'] == 'What is the capital of New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_nz_capital']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_nz_capital']}"

                elif question['question'] == 'Which two islands make up New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_nz_island']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_nz_island']}"

                elif question['question'] == 'What is the name of the highest mountain in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_mountain']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_mountain']}"

                elif question['question'] == 'What is the name of the largest lake in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_lake']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_lake']}"

                elif question['question'] == 'What is the name of the famous geothermal area in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_area']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['correct_area']}"

            #Feedback for the correct answers for Food quiz
            elif self.selected_quiz_topic == 'quiz_foods':
                if question['question'] == 'What is the national dish of New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_cooking_method']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_cooking_method']}"
                elif question['question'] == 'What is the name of the popular New Zealand fruit?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_fruit']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_fruit']}"

                elif question['question'] == 'What is the name of the popular New Zealand drink?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_drink']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_drink']}"

                elif question['question'] == 'What is the name of the popular New Zealand cheese?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_cheese']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_cheese']}"

                elif question['question'] == 'What is the name of the popular New Zealand chocolate?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_chocolate']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['correct_chocolate']}"

        #Feecback for the incorrect answers for the Culture quiz.
        else:
            score_feedback = f"Incorrect. Correct answer: {correct_answer}"
            if self.language == 'japanese':
                score_feedback = "不正解。正解は" + correct_answer + "です。"

            if self.selected_quiz_topic == 'quiz_culture':
                if question['question'] == 'What is the national bird of New Zealand?':
                    if self.language == 'english':
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_bird']}"
                    else:
                            score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_bird']}"

                elif question['question'] == 'What is the traditional Māori greeting?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_greeting']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_greeting']}"

                elif question['question'] == 'What is the name of the traditional Māori dance?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_traditional_dance']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_traditional_dance']}"

                elif question['question'] == 'What is the name of the traditional Māori meeting house?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_house']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_house']}"

                elif question['question'] == 'What is the name of the traditional Māori carving style?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_carving']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_culture']['incorrect_carving']}"


            #Feedback for the incorrect answers for Geography quiz
            elif self.selected_quiz_topic == 'quiz_geography':
                if question['question'] == 'What is the capital of New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_nz_capital']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_nz_capital']}"
                elif question['question'] == 'Which two islands make up New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_nz_island']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_nz_island']}"

                elif question['question'] == 'What is the name of the highest mountain in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_mountain']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_mountain']}"

                elif question['question'] == 'What is the name of the largest lake in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_lake']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_lake']}"

                elif question['question'] == 'What is the name of the famous geothermal area in New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_area']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_geography']['incorrect_area']}"

            #Feedback for the incorrect answers for Food quiz
            elif self.selected_quiz_topic == 'quiz_foods':
                if question['question'] == 'What is the national dish of New Zealand?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_cooking_method']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_cooking_method']}"

                elif question['question'] == 'What is the name of the popular New Zealand fruit?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_fruit']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_fruit']}"

                elif question['question'] == 'What is the name of the popular New Zealand drink?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_drink']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_drink']}"

                elif question['question'] == 'What is the name of the popular New Zealand cheese?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_cheese']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_cheese']}"

                elif question['question'] == 'What is the name of the popular New Zealand chocolate?':
                    if self.language == 'english':
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_chocolate']}"
                    else:
                        score_feedback += f"\n{quiz_feedback[self.language]['quiz_foods']['incorrect_chocolate']}"


        # Display score feedback
        self.label_score_feedback = tk.Label(self.frames["quiz"], text=score_feedback)
        self.label_score_feedback.pack(pady=10)


        # Update score display
        self.label_score.config(text=f"Score: {self.total_score}/{self.current_question_index + 1}")


        # Move to the next question after a delay
        self.current_question_index += 1
        if self.current_question_index < len(quiz_questions[self.language][self.selected_quiz_topic]):
            self.after(4000, self.show_next_question)  # 3-second delay
        else:
            self.after(4000, self.show_final_score)  # 3-second delay

    def show_final_score(self):
        """
        Displays the final score and options to go back to the start or exit.

        This function displays the user's total score and provides buttons
        to either restart the quiz or exit the game.
        """
        # Clear the quiz page frame
        for widget in self.frames["quiz"].winfo_children():
            widget.destroy()

        # Clear the final score frame
        for widget in self.frames["final_score"].winfo_children():
            widget.destroy()

        self.show_page("final_score")

        score_text = f"Your total score is {self.total_score}/{len(quiz_questions[self.language][self.selected_quiz_topic])}"
        self.label_final_score = tk.Label(self.frames["final_score"], text=score_text)
        self.label_final_score.pack(pady=20)

        self.button_go_back_to_start = tk.Button(self.frames["final_score"], text="Go Back to Start", command=self.reset_quiz)
        self.button_go_back_to_start.pack(pady=20)

        self.button_exit = tk.Button(self.frames["final_score"], text="Exit Game", command=self.exit_game)
        self.button_exit.pack(pady=20)

    def reset_quiz(self):
        """
        Resets the quiz to the start page.

        This function resets the score and question index to their initial
        values and returns the user to the start page.
        """
        self.show_start_page()
        self.total_score = 0
        self.current_question_index = 0

    def exit_game(self):
        """Exits the game."""
        self.destroy()

    def setup_start_page(self):
        """
        Sets up the start page with welcome message and buttons.

        This function creates the elements of the start page, including
        a welcome message and buttons to start the game, view instructions,
        or exit.
        """
        self.label_start = tk.Label(self.frames["start"], text="Welcome to the Quiz!")
        self.label_start.pack(pady=20)

        self.button_play = tk.Button(
            self.frames["start"],
            text="Play Game",
            command=self.show_language_page
        )
        self.button_play.pack(pady=20)

        self.button_about_this_game = tk.Button(
            self.frames["start"],
            text="How to play",
            command=self.show_about_this_game_page
        )
        self.button_about_this_game.pack(pady=20)

        self.button_exit = tk.Button(
            self.frames["start"],
            text="Exit Game",
            command=self.exit_game
        )
        self.button_exit.pack(pady=20)

    def setup_language_page(self):
        """
        Sets up the language selection page.

        This function creates the language selection page, allowing the
        user to choose their preferred language for the quiz.
        """
        self.label_language = tk.Label(self.frames["language"], text="Please select a language you comfortably understand")
        self.label_language.pack(pady=20)

        self.button_english_quiz = tk.Button(
            self.frames["language"],
            text="English",
            command=lambda: self.show_quiz_selection_page('english')
        )
        self.button_english_quiz.pack(pady=20)

        self.button_japanese_quiz = tk.Button(
            self.frames["language"],
            text="Japanese",
            command=lambda: self.show_quiz_selection_page('japanese')
        )
        self.button_japanese_quiz.pack(pady=20)

    def setup_about_this_game_page(self):
        """
        Sets up the about this game page.

        This function creates the about this game page, displaying
        instructions on how to play the quiz.
        """
        self.label_about_this_game = tk.Label(
            self.frames["about"],
            text=LOCALIZATION_STRINGS[self.language]['quiz_info'],
            wraplength=350,
            justify="left"
        )
        self.label_about_this_game.pack(pady=20)


        self.button_go_back_to_start = tk.Button(
            self.frames["about"],
            text="Go Back",
            command=self.show_start_page
        )
        self.button_go_back_to_start.pack(pady=20)

    def update_about_page_text(self):
        """
        Updates the text on the about this game page based on the selected language.

        This function ensures that the instructions are displayed in the
        correct language based on the user's selection.
        """
        self.label_about_this_game.config(text=LOCALIZATION_STRINGS[self.language]['quiz_info'])

    def setup_quiz_selection_page(self):
        """
        Sets up the quiz selection page.

        This function creates the quiz selection page, allowing the user
        to choose the topic of the quiz they want to take.
        """
        self.label_select_quiz = tk.Label(self.frames["quiz_selection"], text="Please select a quiz topic")
        self.label_select_quiz.pack(pady=20)

        for topic_key, topic_value in QUIZ_TOPICS.items():
            button = tk.Button(
                self.frames["quiz_selection"],
                text=topic_value,
                command=lambda topic=topic_key: self.start_quiz(topic)
            )
            button.pack(pady=10)

        self.button_go_back = tk.Button(
            self.frames["quiz_selection"],
            text="Go Back",
            command=self.show_language_page
        )
        self.button_go_back.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
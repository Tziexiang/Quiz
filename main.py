# I imported data from another file and added a GUI to the code.
import tkinter as tk
from tkinter import Button
from data import LOCALIZATION_STRINGS, QUIZ_TOPICS, quiz_questions
#The title and the size of the window
import tkinter as tk
class App(tk.Tk):
 def __init__(self):
     super().__init__()
     self.title("My Quiz")
     self.geometry("500x700")
#this is test
# Create a master frame to hold pages
     self.master_frame = tk.Frame(self)
     self.master_frame.pack(fill="both", expand=True)

# Create frames for each page
     self.start_page_frame = tk.Frame(self.master_frame)
     self.language_page_frame = tk.Frame(self.master_frame)
     self.about_this_game_page_frame = tk.Frame(self.master_frame)
     self.quiz_page_frame = tk.Frame(self.master_frame)
     
# Place widgets on the start page
     self.label_start = tk.Label(self.start_page_frame, text="Welcome to the Quiz!")
     self.label_start.pack(pady=20)

     #Buttons for 'Play Game', 'How to play', and 'Exit Game'
     self.button_play = tk.Button(
          self.start_page_frame, 
          text="Play Game", 
          width=35, 
          height=3, 
          command=self.show_language_page
      )
     self.button_play.place(x=95, y=400)


     self.button_about_this_game = tk.Button(
         self.start_page_frame, 
         text="How to play", 
         width=35, height=3, 
         command=self.show_about_this_game_page
     )
     self.button_about_this_game.place(x=95, y=500)


     self.button_exit = tk.Button(
         self.start_page_frame, 
         text="Exit Game", 
         width=35, height=3, 
         command=self.exit_game
     )
     self.button_exit.place(x=95, y=600)

     
# Place widgets on the language page
     self.label_language = tk.Label(self.language_page_frame, text="Please select a language you comfortably understand")
     self.label_language.pack(pady=20)

     self.button_english_quiz = tk.Button(
          self.language_page_frame, 
          text="English", 
          width=20, 
          height=5, 
          command=self.show_quiz_page
      )
     self.button_english_quiz.place(x=35, y=400)


     self.button_japanese_quiz= tk.Button(
         self.language_page_frame, 
         text="Japanese", 
         width=20, 
         height=5, 
         command=self.show_quiz_page
     )
     self.button_japanese_quiz.place(x=230, y=400)

#Place widgets on quiz page
     self.label_quiz = tk.Label(self.quiz_page_frame, text="QUESTIONS")
     self.label_quiz.pack(pady=20)
     
#Place widgets on the how to play page
     self.label_about_this_game = tk.Label(
         self.about_this_game_page_frame, 
         text="This is a quiz game that will test your knowledge of New Zealand. You will be asked a series of questions" + "\n\n" +
         "Here's how to play:\n" +
         "1. Select a quiz topic.\n" +
         "2. Read the question and the answer options.\n" +
         ""
     )
         
     self.label_about_this_game.place(x=100, y=100)

     self.button_go_back = tk.Button(
         self.about_this_game_page_frame,
         text="Go Back",
         width=35, height=3,
         command=self.show_start_page
     )
     self.button_go_back.place(x=95, y=500)
     
# Initially show the start page
     self.show_start_page()

 def show_start_page(self):
    self.start_page_frame.pack(fill="both", expand=True)
    self.language_page_frame.pack_forget()
    self.about_this_game_page_frame.pack_forget()
    
 def show_language_page(self):
    self.language_page_frame.pack(fill="both", expand=True)
    self.start_page_frame.pack_forget()
    self.about_this_game_page_frame.pack_forget()

 def show_about_this_game_page(self):
     self.about_this_game_page_frame.pack(fill="both", expand=True)
     self.start_page_frame.pack_forget()
     self.language_page_frame.pack_forget()

 def show_quiz_page(self):
     self.quiz_page_frame.pack(fill="both", expand=True)
     

 def exit_game(self):
     self.destroy()

if __name__ == "__main__":
 app = App()
 app.mainloop()
        
            
       
#This is a 'how to play' function, which will explain the rules of the quiz.

#-----------------------------
class Quiz:
    def __init__(self, language):
        self.language = language

    def quiz_type(self):
        return input(LOCALIZATION_STRINGS[self.language]['quiz_type_prompt']).lower()

    def quiz_culture(self):
        questions = quiz_questions['quiz_culture']
        total_score = 0

        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            user_answer = input("Your answer (A, B, C, or D): ").lower()
            if user_answer == question['correct_answer']:
                total_score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question['options'][ord(question['correct_answer']) - ord('a')]}\n")

        if self.language == 'english':
            print(f"Your total score is {total_score}/{len(questions)}")
        elif self.language == 'japanese':
            print(f"あなたの合計スコアは {total_score}/{len(questions)}")

    def quiz_geography(self):
        questions = quiz_questions['quiz_geography']
        total_score = 0

        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            user_answer = input("Your answer (A, B, C, or D): ").lower()
            if user_answer == question['correct_answer']:
                total_score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question['options'][ord(question['correct_answer']) - ord('a')]}\n")

        if self.language == 'english':
            print(f"Your total score is {total_score}/{len(questions)}")
        elif self.language == 'japanese':
            print(f"あなたの合計スコアは {total_score}/{len(questions)}")

    def quiz_foods(self):
        questions = quiz_questions['quiz_foods']
        total_score = 0

        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            user_answer = input("Your answer (A, B, C, or D): ").lower()
            if user_answer == question['correct_answer']:
                total_score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question['options'][ord(question['correct_answer']) - ord('a')]}\n")

        if self.language == 'english':
            print(f"Your total score is {total_score}/{len(questions)}")
        elif self.language == 'japanese':
            print(f"あなたの合計スコアは {total_score}/{len(questions)}")


    def play(self):
        name = input(LOCALIZATION_STRINGS[self.language]['greeting'])
        print(LOCALIZATION_STRINGS[self.language]['introduction'].format(name=name))
        print(LOCALIZATION_STRINGS[self.language]['quiz_info'])

        # Ask if the user wants to play
        play = input(LOCALIZATION_STRINGS[self.language]['play_prompt']).lower()
        if play == 'yes' if self.language == 'english' else 'はい':
            # The user wants to play, so start the quiz
            while True:  # Keep playing until the user decides to stop
                quiz_type = self.quiz_type()
                if quiz_type in QUIZ_TOPICS:
                    getattr(self, QUIZ_TOPICS[quiz_type])()
                    play = input(LOCALIZATION_STRINGS[self.language]['play_again_prompt']).lower()
                    if play == 'no' if self.language == 'japanese' else 'いいえ':
                        print(LOCALIZATION_STRINGS[self.language]['bye'])
                        break # Exit the loop 
                    if play == 'yes' if self.language == 'english' else 'はい':
                        # User wants to play again, so continue the loop
                        continue
                    else:
                        # User does not want to play again
                        print(LOCALIZATION_STRINGS[self.language]['bye'])
                        break  # Exit the loop           

                else:
                    print("Invalid quiz type. Please choose from available options. Enter 'Culture', 'Geography', or 'Foods'")
        else:
            # User does not want to play
            print(LOCALIZATION_STRINGS[self.language]['ready'])





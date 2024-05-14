name = input("Hello there! What's your name? ")
print(f"Hello {name}!, before we start, allow me to intruduce you to my quiz.")

print("This quiz is about some helpful information you will need "
      "before moving or visiting New Zealand.")

type = 

def play():
  ready = input('Are you ready to play ' + name + '?')
  if ready in ["yes", "ok", "okay", "go"]:
    print("Let's get started!")
  else:
    print('Come back when you are ready to play.')
    play()

play()

#--------------------------------
def quiz():

  guesses = []
  correct_guesses = 0
  questions_num = 1

  for key in questions:
      print("  ")
      print(key)
      for i in options[questions_num-1]:
          print(i)
      guess = input ("Enter (A, B, C, or  D): ")
      guess = guess.upper()
      guesses.append(guess)

      correct_guesses += check_answer(questions.get(key), guess)
      questions_num += 1

  display_score(correct_guesses, guesses)
  
#--------------------------------

def check_answer(answer, guess):

    if answer == guess:
      print("CORRECT!")
      return 1
    else:
      print("INCORRECT!")
      return 0
      
#--------------------------------
def display_score(correct_guesses, guesses):
    print(" ")
    print("RESULTS")
    print(" ")
  
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
  
    print("Guesses: ", end="")
    for i in guesses:
      print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("Your score is: "+str(score)+"%")
#--------------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
# Asks the user if they want to play again and if not, then the game will end.
    if response == "YES":
      return response == "YES"
    else:
      return response == "YES"


#--------------------------------

#These are the dictionary which consists of the questions and the answers for my quiz.
questions = {
  "1. What is the capital of New Zealand?": "A",
  "2. What is the largest city in New Zealand?": "C",
  "3. What is the name of the steepest mountain in New Zealand?": "B",
  "4. What is the name of the highest mountain in New Zealand?": "D",
  "5. What is the name of the largest lake in New Zealand?": "B",
  "6. What is the name of the largest river in New Zealand?": "B",
  "7. What is the name of the largest island in New Zealand?": "A",
  "8. What is the name of the largest city in New Zealand?": "D",
}

options = [["A. Wellington", "B. Christchurch", "C. Sydney ", "D. Otago"],
         ["A. Christchurch", "B. Otago", "C. Auckland", "D. Wellington"],
         ["A. Belfast", "B. Mount Cook", "C. Northwood", "D. Kiwi"],
         ["A. Mount Cook", "B. Otago", "C. Belfast", "D. Mount Taranaki"],
         ["A. Otago river", "B. Lake Taupo", "C. Lake papa", "D. Papa rich"],
         ["A. Belfast river", "B. Waikato RIver", "C. Steven", "D. Big ofalltime"],
         ["A. South Island", "B. Big Island", "C. Small Island", "D. Medium Island"],
         ["A. Christchurch", "B. Duneden","C. Wellington", "D. Auckland"]]

quiz()

while play_again():
  quiz()

print("Thank you for playing my quiz!")

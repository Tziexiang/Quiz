# Localization strings
LOCALIZATION_STRINGS = {
    'english': {
        # Greeting message for the quiz
        'greeting': "Hello there! What's your name? ",
        # Introduction message after getting the user's name
        'introduction': "Hello {name}! Before we start, allow me to introduce you to my quiz.",
        # Information about the quiz
        'quiz_info': "This quiz is about some helpful information you will need before moving to New Zealand.",
        # Prompt to ask if the user wants to play
        'play_prompt': "Would you like to play? (yes or no) ",
        # Prompt to ask if the user wants to play again
        'play_again_prompt': "Would you like to play again? ",
        # Prompt to ask the user to select a quiz type
        'quiz_type_prompt': "Please select a type of quiz: (Culture, Geography, Foods) ",
        # Message to display the user's total score
        'score_message': "Your total score is {total}.",
        # Message to tell the user to come back when they're ready
        'ready': "Ok, come back when you're ready to play!",
        # Goodbye message after the user finishes playing
        'bye': "Byee! Thank you for playing my quiz!"
    },
    'japanese': {
        # Greeting message for the quiz in Japanese
        'greeting': "こんにちは！あなたの名前は何ですか？ ",
        # Introduction message after getting the user's name in Japanese
        'introduction': "こんにちは {name}! 始める前に、私のクイズを紹介させてください。",
        # Information about the quiz in Japanese
        'quiz_info': "このクイズは、ニュージーランドに移住する前に必要となる役立つ情報に関するものです。",
        # Prompt to ask if the user wants to play in Japanese
        'play_prompt': "プレイしますか？（はい、もしくは、いいえ）",
        # Prompt to ask if the user wants to play again in Japanese
        'play_again_prompt': "プレイしますか？ ",
        # Prompt to ask the user to select a quiz type in Japanese
        'quiz_type_prompt': "クイズの種類を選択してください: (文化、地理、食べ物)",
        # Message to display the user's total score in Japanese
        'score_message': "あなたの合計スコアは {total} です。",
        # Message to tell the user to come back when they're ready in Japanese
        'ready': "はい、遊ぶ準備ができたらまた来てください!",
        # Goodbye message after the user finishes playing in Japanese
        'bye': "バイバイ！私のクイズをプレイしていただきありがとうございます!"
    }
}

# Quiz topics
QUIZ_TOPICS = {
    # English and Japanese mappings for 'Culture' quiz
    'culture': 'quiz_culture',
    '文化': 'quiz_culture',
    # English and Japanese mappings for 'Geography' quiz
    'geography': 'quiz_geography',
    '地理': 'quiz_geography',
    # English and Japanese mappings for 'Foods' quiz
    'foods': 'quiz_foods',
    '食べ物': 'quiz_foods'
}

# Define quiz questions (you can organize these better if needed)
quiz_questions = {
    # Questions for the 'Culture' quiz
    'quiz_culture': [
        {
            # Question 1
            'question': "What is the main culture of New Zealand?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "a"
        },
        {
            # Question 2
            'question': "What is the culture of the people?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "c"
        },
        {
            # Question 3
            'question': "What is culture?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "b"
        }
    ],
    # Questions for the 'Geography' quiz
    'quiz_geography': [
        {
            # Question 1
            'question': "What is the main geography of New Zealand?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "a"
        },
        {
            # Question 2
            'question': "What is the geo of the people?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "c"
        },
        {
            # Question 3
            'question': "What is geo?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "b"
        }

    ],
    # Questions for the 'Foods' quiz
    'quiz_foods': [
        {
            # Question 1
            'question': "What is the main food of New Zealand?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "a"
        },
        {
            # Question 2
            'question': "What is the food of the people?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "c"
        },
        {
            # Question 3
            'question': "What is foods?",
            'options': ["A. asdfasdf", "B. Casdfadsf", "C. asdfasdfsf", "D. sfsafsafs "],
            'correct_answer': "b"
        }
    ]
}
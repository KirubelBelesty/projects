 #list of questions 
 # store the answers
 
 
 # randomly pick questions
 # ask questions 
 # see if they are correct 
 # keep track of the score 
 # tell the user their score 
 
import random 
 
 
 
 
questions = {
      "What is the capital of France?": "paris",
      "What is 2 + 2?": "4",
      "What is the capital of Spain?": "madrid",
      "What is 3 * 5?": "15",
      "What is the capital of Italy?": "rome",
      "What software company is headquartered in Redmond, Washington?": "microsoft",
      "What is a word, phrase, number, or other sequence of characters that reads the same backward as forward?": "palindrome",
      "What is the world’s largest retailer as of 2026?": "walmart",
      "Which day of the week does the Jewish Sabbath begin?": "friday",
      "What phone company produced the 3310?": "nokia",
      "What company was initially known as 'Blue Ribbon Sports'?": "nike",
      "Which country has the highest life expectancy as of 2026?": "monaco",
      "What is the most common surname in the United States?": "smith",
      "What art form is described as 'decorative handwriting or handwritten lettering'?": "calligraphy",
      "What is acrophobia a fear of?": "heights",
      "What is the name of the Chinese philosophical system that emphasizes harmony with nature?": "taoism",
      "What is the 4th letter of the Greek alphabet?": "delta",
      "How many dots appear on a pair of dice?": "42",
      "Who was the Ancient Greek God of the Sun?": "apollo",
      "Aureolin is a shade of what color?": "yellow",
      "How many faces does a Dodecahedron have?": "12",
      "How many minutes are in a full week?": "10,080",
      "December 26 is known by what name in Ireland?": "saint stephen's day"
}

def kira_trivia_games():
   questions_list = list(questions.keys())
   total_questions = 5 
   score = 0

   selected_questions = random.sample(questions_list, total_questions)
   
   for idx, question in enumerate(selected_questions):
       print(f"{idx + 1}. {question}")
       user_answer = input("your answer: ").lower().strip()
       correct_answer = questions[question].lower().strip()

       if user_answer == correct_answer:
           print("Correct!\n")
           score += 1
       else:
           print(f"Wrong! The correct answer is: {correct_answer}\n")

   print(f"Game over! Your final score is: {score}/{total_questions}")

kira_trivia_games()
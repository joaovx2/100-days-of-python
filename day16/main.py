from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
##imports shit


question_bank = []#makes a question_bank using the list of question in the data 
for question in question_data:#loops through the list of questions populating the question_bank variable
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) #calls out the method

while quiz.still_has_questions(): #makes a while loop to check if there is questions remaining
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}") #shows final score and what quesiton did u stop


class QuizBrain:

    def __init__(self, q_list): ##initilizes de class with the question_number 0 and score 0
        self.question_number = 0
        self.score = 0
        self.question_list = q_list #gets the question from the list

    def still_has_questions(self): #method1, will check if there are still questions remaining
        return self.question_number < len(self.question_list) #evaluetes IF the question_number is less than the len of the list, 

    def next_question(self): #method 2, shows the question, and increases the quesiton number
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer) #calls out the method to check the answer that was definied in the class 

    def check_answer(self, user_answer, correct_answer): #checks if the answer is right or wrong, increases the score in case it is 
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else: #shows the correct answer in case you got it wrong
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

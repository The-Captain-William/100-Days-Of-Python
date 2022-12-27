class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        given_question = self.question_list[self.question_number]  # gets question from its own question list
        self.question_number += 1  # increase index by 1; will also display on input. efficient!
        user_answer = input(f"\nQ:{self.question_number} {given_question.text} (True/False?): ").lower()
        if user_answer == "exit":
            exit()
        else:
            self.check_answer(user_answer, given_question.ans)

    # question == self question list[self index]
    # use ".text" b/c it will display textual info

    def still_has_questions(self):
        if self.question_number < len(self.question_list):  # will terminate after last question
            return True  # example, 5<5 == false, stop asking questions
        else:  # if <=, will get out of range error
            return False
        # alternative code -> return self.question_number < len(self.question_list):

    # no need to offset, still has questions will check question number after first question initialised
    # 0, 1, 2, 3, 4, will become 1, 2, 3, 4, 5, with self.question_number +=1 in next_question
    # 1, 2, 3, 4, 5,

    def check_answer(self, user_answer, correct_answer):  # already knows what our answer is from input in main
        if user_answer == correct_answer.lower():  # ❗ make sure incoming data is formatted with .lower()
            self.score += 1
            print("correct!")
        else:
            print("Incorrect.")
        print(f"{self.score}/{len(self.question_list)} correct.")  # alternative is score/question number but will
        # only show 1/1, 1/2, etc.

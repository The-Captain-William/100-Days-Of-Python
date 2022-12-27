from question_model import Question
from data import question_data, question_data_comp
from quiz_brain import QuizBrain

question_bank = []

for question in question_data_comp:  # note capital Q for class object question format
    question_format = Question(question["question"], question["correct_answer"])  # object == object(dict text keyval,
    question_bank.append(question_format)                             # dict ans keyval)

#  print(question_bank[2].text) example of how to call up (object)(index)attribute)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions() is True:
    quiz.next_question()


print("You've completed the quiz!")  # no need for a while loop here, will run when above stops loop
print(f"Your total score is {quiz.score}/{len(quiz.question_list)}, "
      f"{round(quiz.score / len(quiz.question_list) * 100, 2)}%")  # round or you'll get tons of digits




#
# for question in question_data:
#     question_format = Question(question["text"], question["answer"])  # object == object(dict text keyval,
#     question_bank.append(question_format)                             # dict ans keyval)
#
# #  print(question_bank[2].text) example of how to call up (object)(index)attribute)
#
# quiz = QuizBrain(question_bank)
# quiz.next_question()
#
# while quiz.still_has_questions() is True:
#     quiz.next_question()
#
#
# print("You've completed the quiz!")  # no need for a while loop here, will run when above stops loop
# print(f"Your total score is {quiz.score}/{len(quiz.question_list)}, "
#       f"{round(quiz.score / len(quiz.question_list) * 100, 2)}%")  # round or you'll get tons of digits



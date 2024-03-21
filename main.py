from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for obj in question_data:  # scorrere la lista con il dizionario
    question_text = obj["question"]
    question_answer = obj["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.points}/{len(question_bank)}")

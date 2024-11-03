from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionText = question['question']
    questionAnswer = question['correct_answer']
    newQuestion = Question(qText= questionText, qAnswer= questionAnswer)
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print('Thank you for playing!')
print(f"Your final score is {quiz.score}/{quiz.questionNumber}")
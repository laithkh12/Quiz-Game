class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.score = 0
        self.questionList = qList

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(f"Q. {self.questionNumber} -> {currentQuestion.text} (True/False): ")
        self.checkAnswer(userAnswer, currentQuestion.answer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print(f"Correct! {correctAnswer}")
        else:
            print(f"Incorrect! {correctAnswer}")

        print(f"Your score is {self.score}/{self.questionNumber}\n")
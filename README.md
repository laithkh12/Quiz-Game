# 🎉 Quiz Game 🎉

A simple console-based quiz game that tests your knowledge of computers! Answer True or False questions and see how high you can score! 🧠💡

## 📁 Project Structure

This project is organized into four main files:

- **`data.py`**: Contains the questions and answers for the quiz in JSON format.
- **`main.py`**: Main script to set up the quiz game, load questions, and run the quiz loop.
- **`question_model.py`**: Defines the `Question` class, representing each quiz question.
- **`quiz_brain.py`**: Contains the `QuizBrain` class, which handles game logic, question tracking, and scoring.

## 📋 Code Breakdown

### 1. `data.py`

Stores questions in JSON format with the following structure:

```python
question_data = [
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science: Computers",
        "question": "&quot;Windows NT&quot; is a monolithic kernel.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    ...
]
```

### 2. `main.py`
Sets up the quiz, loads questions, and starts the game loop:
```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionText = question['question']
    questionAnswer = question['correct_answer']
    newQuestion = Question(qText=questionText, qAnswer=questionAnswer)
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print('Thank you for playing!')
print(f"Your final score is {quiz.score}/{quiz.questionNumber}")
```

### 3. `question_model.py`
Defines the Question class, which represents each question in the game:
```python
class Question:
    def __init__(self, qText, qAnswer):
        self.text = qText
        self.answer = qAnswer
```

### 4. `quiz_brain.py`
Handles game logic, user interaction, and score tracking:
```python
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
```

## 🚀 Getting Started
1. Clone the Repository:
```bash
git clone https://github.com/your-username/quiz-game.git
cd quiz-game
```
2. Run the Game:
```bash
python main.py
```
3. Play and Enjoy! Answer each question as either "True" or "False" and see your score at the end.

## 📜 License
- This project is licensed under the MIT License. See the LICENSE file for more details.

## 💡 Future Enhancements
- Add more question types (e.g., multiple choice).
- Include difficulty levels (easy, medium, hard).
- Create a graphical interface for the game.



Enjoy the game, and happy quizzing! 🎉




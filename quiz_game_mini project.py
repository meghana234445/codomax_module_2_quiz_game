# Python Quiz Game
# Codomax Digital Solutions - Module 2

print("===== PYTHON QUIZ GAME =====")

questions = [
    {
        "question": "1. Which language are we using?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. display()", "C. print()", "D. show()"],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. @"],
        "answer": "B"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "5. Which keyword is used for a loop?",
        "options": ["A. for", "B. repeat", "C. loop", "D. again"],
        "answer": "A"
    }
]

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if answer == question["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
        print("Correct answer:", question["answer"])

print("\n===== QUIZ RESULT =====")

print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Result: Excellent! 🎉")
elif percentage >= 60:
    print("Result: Good Job! 👍")
elif percentage >= 40:
    print("Result: Keep Practicing! 💪")
else:
    print("Result: Need More Practice! 📚")

print("=======================")
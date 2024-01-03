questions = ["Do you know how to program with Python?",
            "Are you confortable coding in SQL?", 
            "Would you be able to collaborate with your teamates on GitHub?"]

user_answer = []

score = 0


def ask_question(question):
    answer = input(f"{question} (Answer 'yes' or 'no'): ").lower()
    while answer not in ['yes', 'no']:
        print("Answer 'yes' or 'no'.")
        answer = input(f"{question} (Answer 'yes' or 'no'): ").lower()
    return answer

for question in questions:
    user_answer = ask_question(question)
    print(f"You answered : {user_answer}")
    
    if user_answer == 'yes': 
        score = score + 1
                
print("\n le score est de : ", score)     
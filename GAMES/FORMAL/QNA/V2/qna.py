import os
questions, answers, startlives = [], [], 3
lives = startlives
def lives_spelling():
    if lives == 1: return "life"
    else: return "lives"
def create_questions():
    q = input(f"Type in a question then an answer. (Example: My favorite color? Blue) (Type finish to finish) [{len(questions)+1}]\n")
    if q == "finish":
        stf = input("Save this to a file? (Y / N)\n")
        if stf.lower() == "n":
            pass
        else:
            with open("questions.txt", "w") as f:
                for qu in questions:
                    f.write(f"q:{qu}\n")
                for an in answers:
                    f.write(f"a:{an}\n")
        ask_questions(0)
        return
    if q.find("? ") <= 0:
        input("\nCould not find a question mark. (Example of a question: My favorite color? Blue) <--- Blue is the answer.\n")
        create_questions()
    questions.append(f"{q.split('? ')[0]}?")
    answers.append(q.split('? ')[1])
    create_questions()
def ask_questions(q):
    global lives,startlives
    if lives > len(questions):
        startlives = len(questions)
        lives = startlives
    if lives <= 0:
        os.system("cls")
        input(f"You ran out of {lives_spelling()}!\n")
        lives = startlives
        ask_questions(0)
    os.system("cls")
    if q >= len(questions):
        os.system("cls")
        input(f"You won with {lives} {lives_spelling()}!\n")
        os.system("cls")
        exit()
    print(f"You have {lives} {lives_spelling()} left!")
    a = input(f"\n{questions[q]} ({q+1}/{len(questions)})\n")
    if a.lower() == answers[q].lower():
        pass
    else:
        lives -= 1
    ask_questions(q+1)
def ask_cora():
    os.system("cls")
    cora = input("Would you like to create a qna or open it from a file? (Options: Create | Open)\n")
    if cora.lower() == "create":
        os.system("cls")
        create_questions()
    elif cora.lower() == "open":
        os.system("cls")
        try:
            with open("questions.txt", "r") as f:
                for line in f.readlines():
                    if line.startswith("q:"):
                        questions.append(line.split("q:")[1].split("\n")[0])
                    elif line.startswith("a:"):
                        answers.append(line.split("a:")[1].split("\n")[0])
            ask_questions(0)
        except FileNotFoundError:
            input("Can not find file!\n")
            ask_cora()
    else:
        os.system("cls")
        input("Incorrect input!\n")
        ask_cora()

ask_cora()
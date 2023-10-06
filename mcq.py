import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Explore')
cursor = conn.cursor()

def insert_questions(question, op1, op2, op3, op4, correct_op):
    cursor.execute("INSERT INTO questions(question, op1, op2, op3, op4, correct_op) VALUES (?, ?, ?, ?, ?, ?)",
                   (question, op1, op2, op3, op4, correct_op))
    conn.commit()

def retrieve_mcqs():
    cursor.execute("SELECT id, question, op1, op2, op3, op4, correct_op FROM questions")
    mcqs = cursor.fetchall()
    return mcqs

def get_correct_answer(question_id):
    cursor.execute("SELECT correct_op FROM questions WHERE id=?", (question_id,))
    result = cursor.fetchone()
    return result[0] if result else None

insert_questions('What is the capital of France?', 'Paris', 'London', 'Berlin', 'Rome', 1)
insert_questions('Which planet is known as the Red Planet?', 'Mars', 'Venus', 'Jupiter', 'Saturn', 1)

mcqs = retrieve_mcqs()

user_responses = {}


for mcq in mcqs:

    question_id, question, op1, op2, op3, op4, correct_op = mcq


    print(f"\nQuestion {question_id}: {question}")
    print("Options:")
    print(f"1. {op1}")
    print(f"2. {op2}")
    print(f"3. {op3}")
    print(f"4. {op4}")

    user_answer = input("Your answer (1-4): ")
    if int(user_answer) == correct_op:
        print("Your answer is correct!")

    else:
        print("Your answer is incorrect.")


    user_responses[question_id] = {
        'user_answer': user_answer,
        'correct_answer': correct_op
    }
print("\nUser Responses:")
for question_id, response in user_responses.items():
    print(f"Question {question_id}: Your answer - {response['user_answer']}, Correct answer - {response['correct_answer']}")
conn.commit()
conn.close()

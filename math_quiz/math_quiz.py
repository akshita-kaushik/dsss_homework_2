import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Randomly selects an operator from addition, subtraction, or multiplication.
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1, num2, operator):
    """
    Generates a math problem and calculates the correct answer based on the given operator.
    
    Args:
        num1 (int): First number in the operation.
        num2 (int): Second number in the operation.
        operator (str): Operator for the problem ('+', '-', '*').

    Returns:
        tuple: A string representing the problem, and an integer answer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2
    
    return problem, answer

def math_quiz():
    """
    Runs a simple math quiz game, asking the user to solve math problems
    and calculating the score based on correct answers.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = generate_random_operator()

        # Generate problem and answer
        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        # Handle user input and validate it
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')  
    print("What is the result of the expression?")
    
    operations = ['+', '-', '*']
    
    for i in range(3):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        random_operations = random.choice(operations)
        
        if random_operations == '+':
            correct_answer = a + b
        elif random_operations == '-':
            correct_answer = a - b
        else:
            correct_answer = a * b
        
        print(f"Question: {a} {random_operations} {b}")
        try:
            user_input = int(input("Your answer: "))
        except ValueError:
            print("Invalid input.")
            return
        
        if user_input == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

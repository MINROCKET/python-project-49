import random
import math
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')
    print("Find the greatest common divisor of given numbers.")

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        print(f"Question: {num1} {num2}")

        try:
            user_input = int(input("Your answer: "))  
        except ValueError:
            print(f"That's not a valid number! Let's try again, {name}!")
            return  

        correct_answer = math.gcd(num1, num2)

        if user_input == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
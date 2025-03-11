import random
import prompt

#def welcome_user():
 #   name = prompt.string('May I have your name? ')
 #   return f'Hello, {name}!'

def main():
    print("Welcome to the Brain Games!")
  #  welcome_user()
    name = prompt.string('May I have your name? ')
    #return f'Hello, {name}!'
    print('Hello,', name, '!')  
    sum = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    
    while sum < 3:
        
        random_number = random.randint(1, 50)
        print(f'Question: {random_number}')
        
        user_input = input('Your answer:').lower()
    
        if (random_number % 2 == 0 and user_input == "yes") or (random_number % 2 != 0 and user_input == "no"):
            print("Correct!")
            sum += 1
        else:
            print(f"'{user_input}'' is wrong answer ;(. Correct answer was {'no' if random_number % 2 != 0 else 'yes'}.")
            print(f"Let's try again, {name}!")
            break
            
    if sum == 3:
        #print(f"Congratulations, {name}!")
        print("Congratulations,", name, "!")


if __name__ == "__main__":
    main()

import random
def play_number_guessing_game():
    comp=random.randint(1,100)
    attempts=0
    print("---WELCOME TO NUMBER GUESSING GAME---")
    while True:
        try:
            user_input = input("Guess a number (1-100) or press 'q' to quit : ")
            if user_input == "q":
                print(f"The correct number was {comp}. \n THANKS FOR PLAYING THE GAME, GOODBYE")
                break
            user = int(user_input)
            attempts += 1
            if not (1<=user<=100):
                print("Guess a number between 1 and 100")
                continue
            if user==comp:
                print(f"CONGRATULATIONS, you guessed the correct number in '{attempts}' attempts.")
                break
            elif user>=comp:
                print("try a lesser number")
            else: print("try a greater number")
        except ValueError:
            print("Invalid input, please enter a valid integer")
if __name__=="__main__":
    play_number_guessing_game()
import hangman
import guessing_game

def choose_game():
    print("*********************************")
    print("*******Choose your game!*******")
    print("*********************************")

    print("(1) Hangman (2) Guessing Game")

    game = int(input("Which game? "))

    if(game == 1):
        print("Playing Hangman")
        hangman.play()
    elif(game == 2):
        print("Playing Guessing Game")
        guessing_game.play()

if(__name__ == "__main__"):
    choose_game()

import random


def play():
    print_opening_message()
    secret_word = load_secret_word()

    guessed_letters = initialize_guessed_letters(secret_word)
    print(guessed_letters)

    hanged = False
    guessed = False
    mistakes = 0

    while not hanged and not guessed:
        guess = request_guess()

        if guess in secret_word:
            mark_correct_guess(guess, guessed_letters, secret_word)
        else:
            mistakes += 1
            draw_hangman(mistakes)

        hanged = mistakes == 7
        guessed = "_" not in guessed_letters

        print(guessed_letters)

    if guessed:
        print_winner_message()
    else:
        print_loser_message(secret_word)


def draw_hangman(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if mistakes == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistakes == 2:
        print(" |      (_)   ")
        print(" |      /     ")
        print(" |            ")
        print(" |            ")

    if mistakes == 3:
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    if mistakes == 4:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")

    if mistakes == 5:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if mistakes == 6:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistakes == 7:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_winner_message():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):
    print("Oh no, you were hanged!")
    print(f"The word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mark_correct_guess(guess, guessed_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            guessed_letters[index] = letter
        index += 1


def request_guess():
    guess = input("Enter a letter: ")
    guess = guess.strip().upper()
    return guess


def initialize_guessed_letters(word):
    return ["_" for letter in word]


def print_opening_message():
    print("*********************************")
    print("*** Welcome to the Hangman Game! ***")
    print("*********************************")


def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


if __name__ == "__main__":
    play()

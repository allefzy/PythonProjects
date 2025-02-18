import random

def play():

    print("*********************************")
    print("Welcome to the Guessing Game!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    print("Choose the difficulty level:")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("Attempt {} of {}".format(round, total_attempts))

        guess_str = input("Enter a number between 1 and 100: ")
        print("You entered", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("You must enter a number between 1 and 100!")
            continue

        correct = guess == secret_number
        higher = guess > secret_number
        lower = guess < secret_number

        if correct:
            print("You got it right and scored {} points!".format(points))
            break
        else:
            if higher:
                print("You missed! Your guess was higher than the secret number.")
            elif lower:
                print("You missed! Your guess was lower than the secret number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("Game over")

if __name__ == "__main__":
    play()

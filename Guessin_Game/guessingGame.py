import random

def game(guess, number):
    if guess < number:
        return "Too low."
    elif guess > number:
        return "Too high!"
    else:
        return "Correct!"

def main():
    number = random.randint(1, 10)

    while True:
        try:
            guess = float(input("Guess the number (between 1 and 10): "))
            result = game(guess, number)
            print(result)

            if result == "Correct!":
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

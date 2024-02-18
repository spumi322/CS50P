import random
import sys

def main():
    while True:
        try:
            n = input("Level: ")
            n = int(n)
            secret_number = random.randint(1, n)
            while n > 0:
                guess = input("Guess: ")
                guess = int(guess)
                if secret_number > guess:
                    print("Too small!")
                    continue
                elif secret_number < guess:
                    print("Too large!")
                    continue
                else:
                    print("Just right!")
                    sys.exit()
            else:
                raise ValueError
        except ValueError:
            pass

main()
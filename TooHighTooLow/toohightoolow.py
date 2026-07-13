# a simple high low number guessing game.
#
import random

class too_high_too_low:
    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        # self.guesses to be zero
        # Get a number guess from the user (between 1 and 100)
        # Convert the input to an integer
        # Increment the number of guesses by 1
        # Check *if* the guess equals the secret number
        # If correct, print a congratulations message with the number of guesses
        # Exit the loop
        # Check *if* the guess is less than the secret number
        # If so, print "Too low!"
        # Otherwise (the guess must be too high)
        # Print "Too high!"
        # Check *if* the player has made 10 guesses
        # If so, print a message saying they've run out of guesses and reveal the number
        # Exit the loop
        self.number = random.randint(1, 100)
        self.guesses = 0
        pass

    def play(self):
        while True:
            print(f"Shhh! The secret number is {self.number}")
            guess = int(input("Enter a number between 1 and 100 inclusive: "))
            self.guesses += 1
            if (guess == self.number):
                print(f"Congrats! You got it in {self.guesses} guesses")
                break
            elif (guess < self.number):
                print("Too low!")
            else:
                print("Too high!")
        
            if (self.guesses >= 10):
                print("Sad trombone... you ran out of guesses")
                break

def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()

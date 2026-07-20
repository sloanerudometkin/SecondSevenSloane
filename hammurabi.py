import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        #define the starting game state
        population = 100
        bushels = 2800
        acres_owned = 1000
        land_value = 19
        #each year we have to print out summaries:
        starved_last_year = 0
        immigrants_last_year = 5
        harvested_last_year = 3000
        yield_per_acre = 3
        rats_eaten_last_year = 200

        #core game loop
        for year in range(1, 11):
            print(" Welcome to Year {year})")

        input("Press enter to progress to the next year...")

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
       
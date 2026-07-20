import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # INITIAL STATE 
        population = 100
        bushels = 2800
        acres_owned = 1000
        land_value = 19
        
        # to track statistics for summaries
        starved_last_year = 0
        immigrants_last_year = 5
        harvested_last_year = 3000
        yield_per_acre = 3
        rats_eaten_last_year = 200

        for year in range(1, 11):
            def printSummary(self, year, starved, immigrants, population, harvest, yield_per_acre, rats_eaten, acres_owned, land_value, bushels):
                print("\nO great Hammurabi!")
                print(f"You are in year {year} of your ten year rule.")
                print(f"In the previous year {starved} people starved to death.")
                print(f"In the previous year {immigrants} people entered the kingdom.")
                print(f"The population is now {population}.")
                print(f"We harvested {harvest} bushels at {yield_per_acre} bushels per acre.")
                print(f"Rats destroyed {rats_eaten} bushels, leaving {bushels} bushels in storage.")
                print(f"The city owns {acres_owned} acres of land.")
                print(f"Land is currently worth {land_value} bushels per acre.")
            
           # 2. PLAYER INPUT:
            # to buy land
            acres_to_buy = self.askHowManyAcresToBuy(land_value, bushels)
            bushels -= acres_to_buy * land_value
            acres_owned += acres_to_buy
            
            # to sell land if they didnt buy
            if acres_to_buy == 0:
                acres_to_sell = self.askHowManyAcresToSell(acres_owned)
                bushels += acres_to_sell * land_value
                acres_owned -= acres_to_sell
            
            # to feed people
            bushels_fed = self.askHowMuchGrainToFeedPeople(bushels)
            bushels -= bushels_fed
            
            # to plant crops
            acres_planted = self.askHowManyAcresToPlant(acres_owned, population, bushels)
            bushels -= acres_planted * 2  # Cost of 2 bushels per acre to plant
            
            #3. YEAR END CALCS 
            # plague
            plagues = self.plagueDeaths(population)
            population -= plagues
            
            # starved
            starved_last_year = self.starvationDeaths(population, bushels_fed)
            population -= starved_last_year
            
            # check for uprising???
            if self.uprising(population, starved_last_year):
                print("\nO Great Hammurabi, you have been overthrown due to extreme starvation!")
                return
            
            # immigration if no one starved
            if starved_last_year == 0:
                immigrants_last_year = self.immigrants(population, acres_owned, bushels)
                population += immigrants_last_year
            else:
                immigrants_last_year = 0
            
            # harvest
            harvested_last_year = self.harvest(acres_planted, acres_planted * 2)
            # for display: calculation for the yield per acre 
            yield_per_acre = harvested_last_year // acres_planted if acres_planted > 0 else 0
            bushels += harvested_last_year
            
            # Rats
            rats_eaten_last_year = self.grainEatenByRats(bushels)
            bushels -= rats_eaten_last_year
            
            # cost of new land
            land_value = self.newCostOfLand()

        # 4. summary:
        # TODO: Implement finalSummary method and call it here

    # INPUT METHODS:

    def askHowManyAcresToBuy(self, price, bushels):
        # ask till valid input...
        while True:
            try:
                acres = int(input(f"O Great Hammurabi, so how many acres of land are you gonna buy? "))
                if acres < 0:
                    print("yeah so you cant buy a negative amount of land lol.")
                elif acres * price > bushels:
                    print(f"You're such a jest! We have only {bushels} bushels left!")
                else:
                    return acres
            except ValueError:
                print("You've gotta enter a valid whole number silly.")

    def askHowManyAcresToSell(self, acresOwned):
        while True:
            try:
                acres = int(input("O Great Hammurabi, how many acres of land are you gonna sell? "))
                if acres < 0:
                    print("UMMM you can't sell a negative amount of land.")
                elif acres > acresOwned:
                    print(f"You're silly... we own only {acresOwned} acres!")
                else:
                    return acres
            except ValueError:
                print("You've gotta enter a valid whole number.")

    def askHowMuchGrainToFeedPeople(self, bushels):
        while True:
            try:
                fed = int(input("O Great Hammurabi, how much grain are you gonna feed your people? "))
                if fed < 0:
                    print("Well... you cannot feed them negative grain.")
                elif fed > bushels:
                    print(f"Sorry bud... we have only {bushels} bushels in storage!")
                else:
                    return fed
            except ValueError:
                print("You've gotta enter a valid whole number.")

    def askHowManyAcresToPlant(self, acresOwned, population, bushels):
        while True:
            try:
                planted = int(input("O Great Hammurabi, how many acres are you gonna plant with grain? "))
                if planted < 0:
                    print("Soooo you can't plant a negative amount of acres.")
                elif planted > acresOwned:
                    print(f"lol no we only own {acresOwned} acres.")
                elif planted > population * 10:
                    print(f"You're such a jest! Our population of {population} can only farm {population * 10} acres!")
                elif planted * 2 > bushels:
                    print(f"Surely you jest! We only have {bushels} bushels of seed left!")
                else:
                    return planted
            except ValueError:
                print("You've gotta enter a valid whole number.")

    # CALCULATION METHODS AS OUTLINED IN THE TEST

    def plagueDeaths(self, population):
        # if there's a 15% chance of plague, half the population dies
        if self.rand.randint(0, 99) < 15:
            return population // 2
        return 0

    def starvationDeaths(self, population, bushelsFedToPeople):
        people_fed = bushelsFedToPeople // 20
        if people_fed >= population:
            return 0
        return population - people_fed

    def uprising(self, population, howManyPeopleStarved):
        if population == 0:
            return True
        return (howManyPeopleStarved / (population + howManyPeopleStarved)) > 0.45

    def immigrants(self, population, acresOwned, grainInStorage):
        if population == 0:
            return 0
        return int((20 * acresOwned + grainInStorage) / (100 * population) + 1)

    def harvest(self, acres, bushelsUsedAsSeed):
        # yield has to be a random number between 1 and 6 (inclusive))
        yield_rate = self.rand.randint(1, 6)
        return acres * yield_rate

    def grainEatenByRats(self, bushels):
        # if theres a 40% chance of infestation, rats eat 10% to 30% of grain
        if self.rand.randint(0, 99) < 40:
            percent_eaten = self.rand.randint(10, 30)
            return int(bushels * (percent_eaten / 100))
        return 0

    def newCostOfLand(self):
        # do a random  price between 17 and 23 bushels/acre
        return self.rand.randint(17, 23)

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
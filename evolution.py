FOOD_SIZE = 5

class Population: # Population class
    def __init__(self):
        self.added_individuals = 0
        self.removed_individuals = 0 # number of Individuals removed in total this day
        self.slaughtered_individuals = 0 # number of Individuals killed by other Individuals this day
        self.food_eaten = 0

    def setupPopulation(self, population):
        self.population = population # list of Individuals in the Population

class Individual: # Individual class
    def __init__(self, population, size, location, vision_distance, eating_distance):
        self.population = population # the Population the Individual belongs to
        self.size = size
        self.location = location
        self.vision_distance = vision_distance
        self.eating_distance = eating_distance

class Food:
    def __init__(self, location, nutrition):
        self.location = location
        self.nutrition = nutrition

class FoodProducer: # class that creates food each day
    def __init__(self):
        pass

    def spawnFood(self, quantity): # creates food
        for i in range(quantity):

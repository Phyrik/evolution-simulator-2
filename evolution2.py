import random
import math

# constants setup
WIDTH = 1000
HEIGHT = 500
FOOD_SIZE = 5
FOOD_PER_DAY = 5

def distanceBetween(pos_1, pos_2):
    return math.sqrt((pos_2[0] - pos_1[0])**2 + (pos_2[1] - pos_1[1])**2)


class Population:  # Population class
    def __init__(self):
        self.added_individuals = 0
        self.removed_individuals = 0  # number of Individuals removed in total this day
        self.slaughtered_individuals = 0  # number of Individuals killed by other Individuals this day
        self.food_eaten = 0
        self.food_producer = FoodProducer(self)

    def setupPopulation(self, population):
        self.population = population  # list of Individuals in the Population

    def newDay(self):
        self.food_producer.spawnFood(FOOD_PER_DAY)
        for individual in self.population:
            individual.eatFood()
        for individual in self.population:
            individual.location = individual.move()

    
class Individual:  # Individual class
    def __init__(self, population, size, location, vision_distance, eating_distance):
        self.population = population # the Population the Individual belongs to
        self.size = size
        self.location = location
        self.vision_distance = vision_distance
        self.eating_distance = eating_distance
        self.energy = 0

    def eatFood(self):  # makes Individual eat all food within eating_distance pixels of its centre
        self.food_list = self.population.food_producer.food_list

        for food in self.food_list:
            if food.nutrition != 0:
                if distanceBetween(self.location, food.location) <= self.eating_distance:
                    self.energy += food.nutrition
                    del self.food_list[self.food_list.index(food)]
                else:
                    continue
        
        return self.food_list

    def move(self):
        self.food_list = self.population.food_producer.food_list

        for food in self.food_list:
            if food.nutrition != 0:
                print(distanceBetween(self.location, food.location))
                if distanceBetween(self.location, food.location) <= self.vision_distance:
                    print("sb3")
                    return food.location

        return self.location


class Food:
    def __init__(self, location, nutrition):
        self.location = location
        self.nutrition = nutrition
        self.colour = (0, 0, 0)


class FoodProducer:  # class that creates food each day
    def __init__(self, population):
        self.food_list = []
        self.population = population

    def spawnFood(self, quantity):  # creates food
        for i in range(quantity):
            self.food_list.append(Food((random.randint(FOOD_SIZE, (WIDTH - FOOD_SIZE)), random.randint(FOOD_SIZE, (HEIGHT - FOOD_SIZE))), 1))
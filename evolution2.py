import random
import math

# constants setup
WIDTH = 1000
HEIGHT = 500
FOOD_SIZE = 5
REPRODUCE_ENERGY = 4
KILL_ENERGY = 7
MOVING_ENERGY = 1
INDIVIDUAL_SIZE = 10

STARTING_NUMBER_OF_INDIVIDUALS = int(input("How many creatures do you want to spawn on the first day? "))
FOOD_PER_DAY = int(input("How many pieces of food do you want to spawn each day? "))
MUTATING_CHANCE = int(input("What percentage chance do you want there to be of a creature's genes to mutate when it reproduces? "))

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
        '''sets up the Population's population with a list of Individuals'''
        self.population = population  # list of Individuals in the Population

    def newDay(self):
        '''simulates one day'''
        self.food_producer.spawnFood(FOOD_PER_DAY)

        # make Individual eat and move
        for individual in self.population:
            individual.eatFood()
            individual.energy -= 0.1
        for individual in self.population:
            individual.location = individual.move()

        # remove dead Individuals
        for individual in self.population:
            if individual.energy <= 0:
                del self.population[self.population.index(individual)]

        # make Individual reproduce and kill if possible
        for individual in self.population:
            if individual.energy >= REPRODUCE_ENERGY:
                individual.reproduce()
            if individual.energy >= KILL_ENERGY:
                individual.kill()
            if individual.energy >= REPRODUCE_ENERGY:
                individual.reproduce()

    
class Individual:  # Individual class
    def __init__(self, population, size, location, vision_distance, eating_distance, mutating_chance, parent):
        self.population = population  # the Population the Individual belongs to
        self.size = size
        self.location = location
        self.vision_distance = vision_distance
        self.eating_distance = eating_distance
        self.mutating_chance = mutating_chance
        self.energy = 0
        self.offspring_vision_distance = 0
        self.offspring_eating_distance = 0
        self.offspring_mutating_chance = 0
        self.parent = parent

    def eatFood(self):
        '''makes Individual eat all food within eating_distance pixels of its centre'''
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
        '''makes Individual move to the first food it finds within vision_distance pixels of its centre'''
        self.food_list = self.population.food_producer.food_list

        for food in self.food_list:
            if food.nutrition != 0:
                if food.moved_to == 0:
                    if distanceBetween(self.location, food.location) <= self.vision_distance:
                        food.moved_to = 1
                        self.energy -= MOVING_ENERGY
                        return food.location

        return self.location

    def reproduce(self):
        '''makes Individual repoduce with either the same or mutated genes'''
        if random.randint(1, 100) <= self.mutating_chance:
            self.offspring_vision_distance = abs(self.vision_distance + random.randint(-20, 20))
        else:
            self.offspring_vision_distance = self.vision_distance
        if random.randint(1, 100) <= self.mutating_chance:
            self.offspring_eating_distance = abs(self.eating_distance + random.randint(-20, 20))
        else:
            self.offspring_eating_distance = self.eating_distance
        if random.randint(1, 100) <= self.mutating_chance:
            self.offspring_mutating_chance = abs(self.mutating_chance + random.randint(-20, 20))
        else:
            self.offspring_mutating_chance = self.mutating_chance

        self.offspring = Individual(self.population, INDIVIDUAL_SIZE, self.location, self.offspring_vision_distance, self.offspring_eating_distance, self.offspring_mutating_chance, self)
        self.population.population.append(self.offspring)

    def kill(self):
        '''kills an Individual within vision_distance pixels of self's centre and if it is not self's child'''
        for individual in self.population.population:
            if distanceBetween(self.location, individual.location) <= self.vision_distance:
                if individual.parent != self:
                    del self.population.population[self.population.population.index(individual)]



class Food:
    def __init__(self, location, nutrition):
        self.location = location
        self.nutrition = nutrition
        self.colour = (0, 0, 0)
        self.moved_to = 0


class FoodProducer:  # class that creates food each day
    def __init__(self, population):
        self.food_list = []
        self.population = population

    def spawnFood(self, quantity):
        '''creates food'''
        for i in range(quantity):
            self.food_list.append(Food((random.randint(FOOD_SIZE, (WIDTH - FOOD_SIZE)), random.randint(FOOD_SIZE, (HEIGHT - FOOD_SIZE))), 1))
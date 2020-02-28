from evolution2 import *
import pygame
import math
import time

# pygame setup
pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Arial', 16, True, False)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IndividualSurface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
FoodSurface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
pygame.display.set_caption("evolution-simulator-2")

# simulation setup
population = Population()
individual = Individual(population, 10, (WIDTH//2, HEIGHT//2), 50, 20)
population_list = [individual]
population.setupPopulation(population_list)

# mainloop
running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    time.sleep(1)

    # simulator stuff
    population.newDay()
    
    screen.fill((255, 255, 255))

    # draw Individual
    for individual in population.population:
        i = population.population.index(individual)

        pygame.draw.circle(IndividualSurface, (255, 0, 0, 160), population.population[i].location, population.population[i].vision_distance)
        pygame.draw.circle(IndividualSurface, (0, 0, 255, 210), population.population[i].location, population.population[i].eating_distance)
        pygame.draw.circle(IndividualSurface, (0, 0, 0), population.population[i].location, population.population[i].size)

    # draw Foods
    for food in population.food_producer.food_list:
        pygame.draw.circle(FoodSurface, (0, 0, 0), food.location, FOOD_SIZE)

    # draws surfaces
    screen.blit(IndividualSurface, (0, 0))
    screen.blit(FoodSurface, (0, 0))

    # draw text above Individual
    for individual in population.population:
        textSurface = myFont.render(str(individual.energy), False, (0, 0, 0))
        screen.blit(textSurface, (individual.location[0] - 5, individual.location[1] - 50))

    pygame.display.update() # updates window

pygame.quit()
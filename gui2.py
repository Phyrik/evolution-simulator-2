from evolution2 import *
import pygame
import time

# pygame setup
pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Arial', 16, True, False)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
pygame.display.set_caption("evolution-simulator-2")

# simulation setup
population = Population()
population_list = []
for i in range(STARTING_NUMBER_OF_INDIVIDUALS):
    individual = Individual(population, INDIVIDUAL_SIZE, (random.randint(1, WIDTH), random.randint(1, HEIGHT)), 50, 20, MUTATING_CHANCE, None)
    population_list.append(individual)
population.setupPopulation(population_list)

# mainloop
running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    time.sleep(0.5)

    # simulator stuff
    population.newDay()
    
    screen.fill((255, 255, 255))
    surface.fill((255, 255, 255))

    # draw Individual
    for individual in population.population:
        i = population.population.index(individual)

        pygame.draw.circle(surface, (255, 0, 0, 160), individual.location, individual.vision_distance, 2)
        pygame.draw.circle(surface, (0, 0, 255, 210), individual.location, individual.eating_distance, 2)
        pygame.draw.circle(surface, (0, 0, 0), individual.location, individual.size)

    # draw Foods
    for food in population.food_producer.food_list:
        food.moved_to = 0
        if food.colour == (0, 0, 0) and food.nutrition > 0:
            pygame.draw.circle(surface, food.colour, food.location, FOOD_SIZE)

    # draw surfaces
    screen.blit(surface, (0, 0))

    # draw text above Individual
    for individual in population.population:
        textSurface = myFont.render(str(round(individual.energy, 1)), False, (0, 0, 0))
        screen.blit(textSurface, (individual.location[0] - 5, individual.location[1] - 50))

    pygame.display.update() # updates window

pygame.quit()
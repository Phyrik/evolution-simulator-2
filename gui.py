import evolution
import pygame
import math
import time

# constants setup
WIDTH = 1000
HEIGHT = 500

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
pygame.display.set_caption("Evolution Simulator 2")

# simulation setup
population = evolution.Population()
individual = evolution.Individual(population, 10, (WIDTH//2, HEIGHT//2), 50, 20)
population_list = [individual]
population.setupPopulation(population_list)

# mainloop
running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    time.sleep(1)
    
    screen.fill((255, 255, 255))

    # draw Individual
    pygame.draw.circle(surface, (255, 0, 0, 160), (population.population[0].location), population.population[0].vision_distance)
    pygame.draw.circle(surface, (0, 0, 255, 210), (population.population[0].location), population.population[0].eating_distance)
    pygame.draw.circle(surface, (0, 0, 0), (population.population[0].location), population.population[0].size)

    screen.blit(surface, (0, 0)) # draws the surface on the window

    pygame.display.update() # updates window

pygame.quit()
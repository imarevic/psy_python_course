# import pygame modules
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My First PyGame Screen")

# change color of screen and draw everything
screen.fill((255, 0, 0))
pygame.display.flip()

pygame.time.wait(8000)

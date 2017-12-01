# import pygame modules
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My First PyGame Screen")

# fill with purple background
screen.fill((128, 0, 128))

# draw everything
pygame.display.flip()

pygame.time.wait(7000)

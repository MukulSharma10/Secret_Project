import pygame
from sys import exit

pygame.init()

screen_width = 1400
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project Secret!")
clock = pygame.time.Clock()

red = (255, 0, 0)

game_active = True

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
            
    screen.fill(red)
    
    pygame.display.flip()

pygame.quit()
exit()

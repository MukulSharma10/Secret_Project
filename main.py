import pygame
from sys import exit

pygame.init()

screen_width = 1400
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project Secret!")
clock = pygame.time.Clock()

text_font = pygame.font.Font('Secrets.ttf', 100)

#Player init
player_stand = pygame.image.load('player.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (700,600))

player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect(midbottom = (200, 700))

#Enemy init
enemy = pygame.image.load('enemy.png').convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (700, 700) )

game_name = text_font.render("Secret Lair", False, "Red")
game_name_rect = game_name.get_rect(center=(700,100))

game_inst = text_font.render("Press Space to Start", False, "White")
game_inst_rect = game_inst.get_rect(center=(700,300))

game_active = False

while True:
    #Handling keydown events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill("Green")    
                    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
    if game_active:
        pass
    
    else:
        #Home screen
        screen.fill('Black')
        screen.blit(game_name, game_name_rect)
        screen.blit(game_inst, game_inst_rect)
        screen.blit(player_stand, player_stand_rect)
    
    pygame.display.update()
    clock.tick(60)
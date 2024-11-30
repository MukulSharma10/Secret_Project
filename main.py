import pygame
from sys import exit

pygame.init()

screen_width = 1400
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project Secret!")
clock = pygame.time.Clock()

text_font = pygame.font.Font('Secrets.ttf', 100)

#Background image
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

#Player init
player_stand = pygame.image.load('player.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (700,600))

player_speed = 10

player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_rect.topleft = (screen_width//2, screen_height//2)

#Enemy init
enemy = pygame.image.load('enemy.png').convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (700, 700) )

game_name = text_font.render("Secret Lair", False, "Red")
game_name_rect = game_name.get_rect(center=(700,100))

game_inst = text_font.render("Press Space to Start", False, "White")
game_inst_rect = game_inst.get_rect(center=(700,300))

def home():
    
    running = True
    
    while running:
        
        screen.fill("Black")
        screen.blit(game_name, (screen_width//2 - game_name.get_width()//2, 200))
        screen.blit(game_inst, (screen_width//2 - game_inst.get_width()//2, 400))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def main_game():
    
    running = True
    while running:
    
        pygame.time.delay(30)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed  
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed  
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed 
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed 
        
        player_rect.x = max(0, min(screen_width - player_rect.width, player_rect.x))
        player_rect.y = max(0, min(screen_height - player_rect.height, player_rect.y))
    
        screen.blit(background, (0,0))
        screen.blit(player, player_rect)
        pygame.display.update()


home()
main_game()
pygame.quit()
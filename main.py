import pygame
import math
import random
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

game_name = text_font.render("Secret Lair", False, "Red")
game_name_rect = game_name.get_rect(center=(700,100))

game_inst = text_font.render("Press Space to Start", False, "White")
game_inst_rect = game_inst.get_rect(center=(700,300))

def win_screen():
    running = True
    while running:
        screen.fill("Black")
        win_text = text_font.render("You Win!", True, "White")
        
        screen.blit(win_text, (screen_width//2 - win_text.get_width()//2, 200))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
    
def enemy_movement(enemy_rect, player_rect, speed):
    dx = player_rect.centerx - enemy_rect.centerx
    dy = player_rect.centery - enemy_rect.centery
    distance = math.sqrt(dx **2 + dy **2)
    if distance != 0:
        dx /= distance
        dy /= distance
    enemy_rect.x += dx * speed
    enemy_rect.y += dy * speed
        
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
    
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy = pygame.transform.scale(enemy, (50,50))
    enemies = []
    enemy_speed = 2
    
    for _ in range(5):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        enemies.append(pygame.Rect(x,y,50,50))
    
    game_duration = 60000
    start_time = pygame.time.get_ticks()
    
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
    
        for enemy_rect in enemies:
            enemy_movement(enemy_rect, player_rect, enemy_speed)
        
        for enemy_rect in enemies:
            if player_rect.colliderect(enemy_rect):
                print("Collision!")
                # running = False

        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, game_duration - elapsed_time)
        if remaining_time == 0:
            running = False
            win_screen()
        
        screen.blit(background, (0,0))
        screen.blit(player, player_rect)
        for enemy_rect in enemies:
            screen.blit(enemy, enemy_rect)
        
        timer_text = text_font.render(f"Time Left: {remaining_time//1000}s", True, "White")    
        screen.blit(timer_text, (10, 10))
            
        pygame.display.update()

home()
main_game()
pygame.quit()
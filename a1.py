import random
import math
import pygame
scrWidth=800
scrHeight=700
player_start_x=350
player_start_y=350
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
pygame.init()
screen=pygame.display.set_mode((scrWidth,scrHeight))
background=pygame.image.load("background.png")
pygame.display.set_caption("Space Invader game")
playerImg=pygame.image.load("player.png")
playerX=player_start_x
playerY=player_start_y
playerX_change=0
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.img.load("enemy.png"))
    enemyX.append(random.randint(0,scrWidth-64))#enemy_width=64
    enemyX.append(random.randint(enemy_start_y_min,enemy_start_y_max))#enemy_width=64
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
BullletY=player_start_y
bulletX_change=0
bulletY_change=bullet_speed_y
bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',30)
textX=10
textY=10
over_font=pygame.font.Font('freesansbold.ttf',60)

def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER"True,(255,255,255))
    screen.blit(over_text,(200,250))
def player():
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))


















bulletImg=pygame.image.load()
bulletX=0
bulletY=
import pygame
from pygame.locals import *
import random
import math

pygame.init()

width = 1000
height = 650
screen = pygame.display.set_mode((width,height))

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0 , 0)
pink = (255, 16, 240)
white = (250,250,250)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)
score_font = pygame.font.SysFont(None, 60)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 60)
#play_again_rect = Rect(300, 400, 300, 100) old play again rectangle
play_again_rect = Rect(350, 500, 300, 100)
game_screen_rect = Rect(95,47.5,815,406)
ready_rect = Rect(350, 500, 300, 100)
score_rect = Rect(50,525,300,100)

pygame.draw.rect(screen,white,game_screen_rect)
shape = [(97,50),(177,50),(177,130),(97,130)]
start_x = 99.5
start_y = 50
length = 75
gap = 81.2

rectangles = {}

j = 0
for k in range(5):
    for i in range(10):
        array = [
            (start_x + gap*i, start_y + gap*k),
            (start_x + length + gap*i, start_y + gap*k),
            (start_x + length + gap*i, start_y + length + gap*k),
            (start_x + gap*i, start_y + length + gap*k)
        ]

        rectangles[j] = array
        j += 1

def generate_polygons():
    sample = random.sample(range(0,50), 50)

    for samp in sample:
        pygame.draw.polygon(screen,blue,rectangles[samp])



generate_polygons()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)
    pygame.display.update()

pygame.quit()
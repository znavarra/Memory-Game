import pygame
from pygame.locals import *
import random
import math

pygame.init()

width = 1000
height = 700
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0 , 0)
font = pygame.font.SysFont(None, 40)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 60)
play_again_rect = Rect(300, 300, 300, 100)
ready_rect = Rect(350, 500, 300, 100)

hexes = {}
clicked = {}
order = {}
sample = []
r = 50
count = 0
for k in range(5):
    
    if k%2 == 1:
        x = 40
        z = 11
    else:
        x = 85
        z = 10
    
    for j in range(z):
        array = [
            (
                round(x + 90*j + r * math.cos(math.pi / 3 * i - math.pi / 2),1),
                round(96 + 77 * k + r * math.sin(math.pi / 3 * i - math.pi / 2),1)
            )
            for i in range(6)
        ]

        hexes[count] = array
        clicked[count] = False
        count += 1

screen = pygame.display.set_mode((width,height))

def generate_polygons(num):
    
    global sample, order, clicks

    clicks = 0
    order = {}
    sample = []
    sample = random.sample(range(0,52), num)

    label = 1
    for samp in sample: 
        pygame.draw.polygon(screen, blue, hexes[samp]) #producing tiles
        
        order[samp] = label #producing tile numbers
        label_text = f"{label}"
        label_img = font.render(label_text, True, green)
        screen.blit(label_img, (hexes[samp][0][0] - 7, ((hexes[samp][1][1] + hexes[samp][2][1]) / 2) - 10))
        clicked[samp] = False
        label += 1

def play_again():
    global game_over
    screen.fill(black)
    game_over_text = "Game Over"
    game_over_img = game_over_font.render(game_over_text, True, red)
    screen.blit(game_over_img, (300,150))

    pygame.draw.rect(screen,red,play_again_rect)
    play_again_text = "Play Again"
    play_again_img = play_again_font.render(play_again_text, True, black)
    screen.blit(play_again_img, (325,325))
    game_over = True
    

def is_point_in_polygon(point, polygon):
    x, y = point
    inside = False
    px, py = polygon[-1]  # Last vertex
    for nx, ny in polygon:
        if (ny > y) != (py > y):  # Check if point is between y-bounds
            if x < (nx - px) * (y - py) / (ny - py + 1e-10) + px:
                inside = not inside
        px, py = nx, ny
    return inside

def ready():
    pygame.draw.rect(screen,blue,ready_rect)
    ready_text = "Ready"
    ready_img = play_again_font.render(ready_text, True, green)
    screen.blit(ready_img, (430,530))
    
clicks = 0
run = True
number = 1
game_over = False
ready_click = False

generate_polygons(number)
ready()

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        #if event.type == pygame.mouse.get_pressed()[0] == True:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()

            if ready_rect.collidepoint(pos) and ready_click == False:
                
                for hex in sample:

                    pygame.draw.polygon(screen,blue,hexes[hex])
                
                ready_click = True
                pygame.draw.rect(screen,black,ready_rect)

            if ready_click == True:

                for hex in sample:

                    if is_point_in_polygon(pos, hexes[hex]) == True and clicked[hex] == False:
                        
                        clicks += 1
                        if clicks == order[hex]:
                            pygame.draw.polygon(screen,black,hexes[hex])
                            clicked[hex] = True

                        elif clicks != order[hex]:
                            play_again()

                        if clicks == number:
                            number += 1
                            generate_polygons(number)
                            ready_click = False
                            ready()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_over is True:
            
            pos = pygame.mouse.get_pos()

            if play_again_rect.collidepoint(pos):

                screen.fill(black)
                number = 1
                generate_polygons(number)
                ready()
                game_over = False
                ready_click = False
    

    pygame.display.update()

pygame.quit()
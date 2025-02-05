import pygame
from pygame.locals import *
import random
import math

pygame.init()

# Fix scoring mechanism when first round is failed

width = 1000
height = 650
screen = pygame.display.set_mode((width,height))

#Colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0 , 0)
pink = (255, 16, 240)
white = (250,250,250)

#Global Variables
sample = []
order = {}
clicked = {}
clicks = 0
ready_click = False
game_over = False
number = 4
strike = 0
strike_state = False

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)
score_font = pygame.font.SysFont(None, 60)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 60)
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
    global sample, order, clicked
    sample = []
    order = {}
    clicked = {}
    sample = random.sample(range(0,50), number)

    label = 1
    for samp in sample:
        pygame.draw.polygon(screen,blue,rectangles[samp])
        order[samp] = label
        clicked[samp] = False
        label_text = f"{label}"
        label_img = font.render(label_text, True, green)
        screen.blit(label_img, (rectangles[samp][0][0]+30, ((rectangles[samp][1][1] + rectangles[samp][2][1])/2) - 10))
        label += 1

def is_point_in_polygon(point,polygon):
    x, y = point
    inside = False
    px, py = polygon[-1]
    for nx, ny in polygon:
        if (ny > y) != (py > y):
            if x < (nx - px) * (y - py) / (ny - py + 1e-10) + px:
                inside = not inside
        px, py = nx, ny
    return inside

def ready():
    pygame.draw.rect(screen, blue, ready_rect)
    ready_text = "Ready"
    ready_img = play_again_font.render(ready_text, True, green)
    screen.blit(ready_img, (435,530))

def play_again():
    global game_over
    screen.fill(black)
    game_over_text = "Game Over"
    game_over_img = game_over_font.render(game_over_text, True, red)
    screen.blit(game_over_img, (310,150))
    final_score_text = f"Final Score: {number - 1}"
    final_score_img = game_over_font.render(final_score_text, True, red)
    screen.blit(final_score_img, (273.5,225))
    game_over = True

def score():
    pygame.draw.rect(screen, black, score_rect)
    score_text = f"Score: {number}"
    score_img = score_font.render(score_text, True, blue)
    screen.blit(score_img, (50, 525))

def strikes():
    global strike
    strike += 1
    screen.fill(black)

    strike_text = f"Strike {strike}"
    strike_img = game_over_font.render(strike_text, True, blue)
    screen.blit(strike_img, (375,200))
    if strike == 3:
        play_again()

generate_polygons()
ready()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if ready_rect.collidepoint(pos) and ready_click == False:

                for samp in sample:
                    pygame.draw.polygon(screen,blue,rectangles[samp])
                    
                ready_click = True
            
            if ready_click == True:
                for samp in sample:
                    val = is_point_in_polygon(pos,rectangles[samp])

                    if val == True and clicked[samp] == False:
                        clicks += 1
                        clicked[samp] = True
                        if clicks == order[samp]:
                            pygame.draw.polygon(screen, white, rectangles[samp])
                            clicked[samp] == True
                        else:
                            ready_click = False
                            clicks = 0
                            strikes()
                            strike_state = True

                if clicks == number:
                    ready_click = False
                    clicks = 0
                    score()
                    number += 1
                    ready()
                    generate_polygons()

            if strike_state == True and game_over == False:

                pygame.draw.rect(screen,blue,ready_rect)
                continue_text = "Continue"
                continue_img = play_again_font.render(continue_text, True, green)
                screen.blit(continue_img, (407.5,530))

                if ready_rect.collidepoint(pos):
                    strike_state = False
                    ready_click = False
                    screen.fill(black)
                    pygame.draw.rect(screen,white,game_screen_rect)
                    score()
                    generate_polygons()
                    ready()
                    

    pygame.display.update()

pygame.quit()


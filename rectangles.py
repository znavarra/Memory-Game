import pygame
from pygame.locals import *
import random
import math
import runpy

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
font = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 60)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 60)
#play_again_rect = Rect(300, 400, 300, 100) old play again rectangle
play_again_rect = Rect(350, 500, 300, 100)
game_screen_rect = Rect(95,47.5,815,415)
ready_rect = Rect(350, 500, 300, 100)
score_rect = Rect(50,525,300,100)

pygame.draw.rect(screen,white,game_screen_rect)

time = []
hexes = {}
clicked = {}
order = {}
sample = []
scored = 0

start_x = 99.5
start_y = 53.5
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



def generate_polygons(number):
    global sample, order, clicks, correct
    clicks = 0
    correct = 0
    order = {}
    sample = []
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

def play_again():
    global game_over
    screen.fill(black)
    game_over_text = "Game Over"
    final_score_text = f"Final Score: {scored}"
    game_over_img = game_over_font.render(game_over_text, True, red)
    final_score_img = game_over_font.render(final_score_text, True, red)
    screen.blit(game_over_img, (310,150))
    screen.blit(final_score_img, (273.5,225))


    pygame.draw.rect(screen,red,play_again_rect)
    play_again_text = "Play Again"
    play_again_img = play_again_font.render(play_again_text, True, black)
    screen.blit(play_again_img, (395,530))
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
    screen.blit(ready_img, (435,530))

def score(clicks):
    global scored
    scored = clicks
    pygame.draw.rect(screen,black,score_rect)
    score_text = f"Score: {clicks}"
    score_img = score_font.render(score_text, True, blue)
    screen.blit(score_img, (50,525))

def next_round():
    global strike, ready_click, scored, next_round_state
    next_round_state = True
    screen.fill(black)

    strike_text = f"Correct: {correct}"
    strike_img = game_over_font.render(strike_text, True, red)
    screen.blit(strike_img, (375,200))

def timer():
    current_time = pygame.time.get_ticks()
    duration = current_time - start_time
    ready_time = [duration,scored]
    time.append(ready_time)
    
clicks = 0
start_time = 0
current_time = 0
run = True
number = 4
correct = 0
game_over = False
ready_click = False
strike = 0
next_round_state = False

generate_polygons(number)
score(0)
ready()

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\landing page.py")
            run = False

        #if event.type == pygame.mouse.get_pressed()[0] == True:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()
            #print(pos)

            if ready_rect.collidepoint(pos) and ready_click == False:

                timer()
                
                for hex in sample:

                    pygame.draw.polygon(screen,blue,rectangles[hex])
                
                ready_click = True
                pygame.draw.rect(screen,black,ready_rect)

            if ready_click == True:

                for hex in sample:

                    if is_point_in_polygon(pos, rectangles[hex]) == True and clicked[hex] == False:
                        
                        clicks += 1
                        if clicks == order[hex]:
                            pygame.draw.polygon(screen,white,rectangles[hex])
                            clicked[hex] = True
                            correct += 1
                        
                        if clicks != order[hex]:
                            pygame.draw.polygon(screen,white,rectangles[hex])

                        if clicks == number:
                            if correct == clicks:
                                score(correct)
                            number += 1
                            start_time = pygame.time.get_ticks()
                            print(correct)
                            next_round()

        if next_round_state == True:

            pygame.draw.rect(screen,blue,ready_rect)
            continue_text = "Continue"
            continue_img = play_again_font.render(continue_text, True, green)
            screen.blit(continue_img, (407.5,530))

            if ready_rect.collidepoint(pos):
                start_time = pygame.time.get_ticks()
                next_round_state = False
                ready_click = False
                screen.fill(black)
                pygame.draw.rect(screen,white,game_screen_rect)
                score(scored)
                generate_polygons(number)
                ready()

        if number == 21:
            play_again()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_over is True:
            
            pos = pygame.mouse.get_pos()

            if play_again_rect.collidepoint(pos):

                screen.fill(black)
                pygame.draw.rect(screen,white,game_screen_rect)
                score(0)
                number = 4
                generate_polygons(number)
                ready()
                game_over = False
                ready_click = False
                strike_state = False
                strike = 0
                start_time = 0
    

    pygame.display.update()

pygame.quit()

print(time)
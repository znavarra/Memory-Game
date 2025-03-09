import pygame
from pygame.locals import *
import random
import math
import runpy
import pandas as pd
import config

scores = pd.read_csv('scores.csv', header = 0)
times = pd.read_csv('times.csv', header = 0)
round_score = [config.CONFIG["unique_id"], config.CONFIG["treatment"]]
time = [config.CONFIG["unique_id"], config.CONFIG["treatment"]]

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


hexes = {}
clicked = {}
order = {}
sample = []
scored = 0
r = 60
count = 0

for k in range(4):
    
    if k%2 == 1:
        x = 172.5 * 1.2
        z = 7
    else:
        x = 127.5 * 1.2
        z = 7
    
    for j in range(z):
        array = [
            (
                round(x + 108*j + r * math.cos(math.pi / 3 * i - math.pi / 2),1),
                round(113.5 + 92.4 * k + r * math.sin(math.pi / 3 * i - math.pi / 2),1)
            )
            for i in range(6)
        ]

        hexes[count] = array
        clicked[count] = False
        count += 1


def generate_polygons(num): 
    
    global sample, order, clicks, correct

    clicks = 0
    correct = 0
    order = {}
    sample = []
    sample = random.sample(range(0,28), num)

    label = 1
    for samp in sample: 
        pygame.draw.polygon(screen, blue, hexes[samp]) #producing tiles
        
        order[samp] = label #producing tile numbers
        label_text = f"{label}"
        label_width, label_height = font.size(label_text)

        # Compute the center of the shape
        shape_x = sum([point[0] for point in hexes[samp]]) / len(hexes[samp])
        shape_y = sum([point[1] for point in hexes[samp]]) / len(hexes[samp])

        # Adjust the label position to center it
        label_x = shape_x - (label_width / 2)
        label_y = shape_y - (label_height / 2)

        label_img = font.render(label_text, True, green)
        screen.blit(label_img, (label_x, label_y+2))
        clicked[samp] = False
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
    ready_time = duration
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
            runpy.run_path("user interface.py")
            run = False

        #if event.type == pygame.mouse.get_pressed()[0] == True:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()
            #print(pos)

            if ready_rect.collidepoint(pos) and ready_click == False:

                timer()
                
                for hex in sample:

                    pygame.draw.polygon(screen,blue,hexes[hex])
                
                ready_click = True
                pygame.draw.rect(screen,black,ready_rect)

            if ready_click == True:

                for hex in sample:

                    if is_point_in_polygon(pos, hexes[hex]) == True and clicked[hex] == False:
                        
                        clicks += 1
                        if clicks == order[hex]:
                            pygame.draw.polygon(screen,white,hexes[hex])
                            clicked[hex] = True
                            correct += 1
                        
                        if clicks != order[hex]:
                            clicked[hex] = True
                            pygame.draw.polygon(screen,white,hexes[hex])

                        if clicks == number:
                            if correct == clicks:
                                score(correct)
                            number += 1
                            start_time = pygame.time.get_ticks()
                            print(correct)
                            round_score.append(correct)
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
            new_row = pd.DataFrame([round_score], columns = scores.columns)
            file = pd.concat([scores,new_row], ignore_index = True)
            file.to_csv('scores.csv', index = False)

            new_time = pd.DataFrame([time], columns = times.columns)
            file_time = pd.concat([times,new_time], ignore_index = True)
            file_time.to_csv('times.csv', index = False)
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
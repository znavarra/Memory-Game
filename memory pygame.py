import pygame
from pygame.locals import *
import random
import math

pygame.init()

width = 1000
height = 500
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont(None, 40)

r = 50

hexes = {}
order = {}

sample = random.sample(range(0,52), 10)

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
        count += 1

screen = pygame.display.set_mode((width,height))

for hex in list(hexes.keys()):
    if hex in sample:
        pygame.draw.polygon(screen, blue, hexes[hex])

label = 1
for samp in sample:
    order[samp] = label
    label_text = f"{label}"
    label_img = font.render(label_text, True, green)
    screen.blit(label_img, (hexes[samp][0][0] - 7, ((hexes[samp][1][1] + hexes[samp][2][1]) / 2) - 10))
    label += 1

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


run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        #if event.type == pygame.mouse.get_pressed()[0] == True:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()

            for hex in sample:

                if is_point_in_polygon(pos, hexes[hex]) == True:
                    
                    print("inside")
                
                elif is_point_in_polygon(pos, hexes[hex]) == False:

                    print("outside")
                    # if colors[hex] == blue:
                    #     color = red
                    #     colors[hex] = color
                    #     pygame.draw.polygon(screen, color, hexes[hex])
                    # else:
                    #     color = blue
                    #     colors[hex] = color
                    #     pygame.draw.polygon(screen, color, hexes[hex])

    

    pygame.display.update()

pygame.quit()
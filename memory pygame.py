import pygame
from pygame.locals import *

pygame.init()

width = 1000
height = 500
blue = (0, 0, 255)
red = (255, 0, 0)

hex_points = [
    (200, 250),  # Left middle
    (225, 206.7),  # Top left
    (275, 206.7),  # Top right
    (300, 250),  # Right middle
    (275, 293.3),  # Bottom right
    (225, 293.3),  # Bottom left
]

hex_points1 = [
    (200, 350),  # Left middle
    (225, 306.7),  # Top left
    (275, 306.7),  # Top right
    (300, 350),  # Right middle
    (275, 393.3),  # Bottom right
    (225, 393.3),  # Bottom left
]

colors = {
    0: blue,
    1: blue,
    2: blue,
    3: blue,
    4: blue,
    5: blue
}

hexes = {0: hex_points}
count = 1

for x in range(10):
    params = []

    for i in hex_points:
        params.append((i[0] + (count *105),i[1]))
    
    hexes[count] = params
    count += 1

screen = pygame.display.set_mode((width,height))


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
color = blue

#pygame.draw.polygon(screen, color, hex_points)

for hex in list(hexes.keys()):
    pygame.draw.polygon(screen, color, hexes[hex])

pygame.draw.polygon(screen, color, hex_points1)

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        #if event.type == pygame.mouse.get_pressed()[0] == True:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()

            for hex in list(hexes.keys()):

                if is_point_in_polygon(pos, hexes[hex]) == True:

                    if colors[hex] == blue:
                        color = red
                        colors[hex] = color
                        pygame.draw.polygon(screen, color, hexes[hex])
                    else:
                        color = blue
                        colors[hex] = color
                        pygame.draw.polygon(screen, color, hexes[hex])

    

    pygame.display.update()

pygame.quit()
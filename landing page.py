import pygame
from pygame.locals import *
import runpy

pygame.init()

width = 1000
height = 650
screen = pygame.display.set_mode((width,height))

font = pygame.font.SysFont(None, 70)
blue = (0, 0, 255)
white = (250,250,250)

choice1_rect = Rect(200,50,200,100)
pygame.draw.rect(screen,blue,choice1_rect)
choice1_text = "1"
choice1_img = font.render(choice1_text, True, white)
screen.blit(choice1_img, (285,75))

choice2_rect = Rect(600,50,200,100)
pygame.draw.rect(screen,blue,choice2_rect)
choice2_text = "2"
choice2_img = font.render(choice2_text, True, white)
screen.blit(choice2_img, (685,75))

choice3_rect = Rect(200,200,200,100)
pygame.draw.rect(screen,blue,choice3_rect)
choice3_text = "3"
choice3_img = font.render(choice3_text, True, white)
screen.blit(choice3_img, (285,225))

choice4_rect = Rect(600,200,200,100)
pygame.draw.rect(screen,blue,choice4_rect)
choice4_text = "4"
choice4_img = font.render(choice4_text, True, white)
screen.blit(choice4_img, (685,225))

choice5_rect = Rect(200,350,200,100)
pygame.draw.rect(screen,blue,choice5_rect)
choice5_text = "5"
choice5_img = font.render(choice5_text, True, white)
screen.blit(choice5_img, (285,375))

choice6_rect = Rect(600,350,200,100)
pygame.draw.rect(screen,blue,choice6_rect)
choice6_text = "6"
choice6_img = font.render(choice6_text, True, white)
screen.blit(choice6_img, (685,375))

choice7_rect = Rect(200,500,200,100)
pygame.draw.rect(screen,blue,choice7_rect)
choice7_text = "7"
choice7_img = font.render(choice7_text, True, white)
screen.blit(choice7_img, (285,525))

choice8_rect = Rect(600,500,200,100)
pygame.draw.rect(screen,blue,choice8_rect)
choice8_text = "8"
choice8_img = font.render(choice8_text, True, white)
screen.blit(choice8_img, (685,525))

run = True

while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if choice1_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\hexes.py")
                pygame.quit()

            if choice2_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\rectangles.py")
                pygame.quit()

            if choice3_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\larger hexes.py")
                pygame.quit()

            if choice4_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\larger rectangles.py")
                pygame.quit()

            if choice5_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\hexes varying colors.py")
                pygame.quit()

            if choice6_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\rectangles varying colors.py")
                pygame.quit()

            if choice7_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\larger hexes varying colors.py")
                pygame.quit()

            if choice8_rect.collidepoint(pos):
                runpy.run_path("C:\\Users\\Zeddrex Navarra\\Desktop\\Career\\Projects\\Memory Game\\Memory-Game\\larger rectangles varying colors.py")
                pygame.quit()
    
    pygame.display.update()

pygame.quit()

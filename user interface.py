import pygame
import sys

pygame.init()

width, height = 1000, 650
screen = pygame.display.set_mode((width, height))

base_font = pygame.font.Font(None, 40)
label_font = pygame.font.Font(None, 50)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')

input_fields = [
    {"label": "Name:", "rect": pygame.Rect(400, 50, 300, 50), "text": "", "active": False},
    {"label": "Year:", "rect": pygame.Rect(400, 125, 300, 50), "text": "", "active": False},
    {"label": "Course:", "rect": pygame.Rect(400, 200, 300, 50), "text": "", "active": False},
    {"label": "Email:", "rect": pygame.Rect(400, 275, 300, 50), "text": "", "active": False},
    {"label": "GCash:", "rect": pygame.Rect(400, 350, 300, 50), "text": "", "active": False}
]

run = True

while run:
    screen.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for field in input_fields:
                if field["rect"].collidepoint(event.pos):
                    for f in input_fields:
                        f["active"] = False
                    field["active"] = True
                    break
            else:
                for field in input_fields:
                    field["active"] = False

        if event.type == pygame.KEYDOWN:
            for field in input_fields:
                if field["active"]:
                    if event.key == pygame.K_BACKSPACE:
                        field["text"] = field["text"][:-1]
                    else:
                        field["text"] += event.unicode

    for field in input_fields:
        pygame.draw.rect(screen, color_active if field["active"] else color_passive, field["rect"])

        label_width, _ = label_font.size(field["label"])
        label_x = field["rect"].x - (label_width + 10)
        
        label_surface = label_font.render(field["label"], False, (255, 255, 255))
        screen.blit(label_surface, (label_x, field["rect"].y + 5))
        
        input_surface = base_font.render(field["text"], True, (255, 255, 255))
        screen.blit(input_surface, (field["rect"].x + 5, field["rect"].y + 10))

        field["rect"].w = max(300, input_surface.get_width() + 10)

    pygame.display.flip()

pygame.quit()

for fields in input_fields:
    print(fields["text"])
import pygame
import sys
import runpy
import pandas as pd

pygame.init()

width, height = 1000, 650
screen = pygame.display.set_mode((width, height))

base_font = pygame.font.Font(None, 35)
label_font = pygame.font.Font(None, 50)
sex_at_birth = pygame.font.Font(None, 40)
corrective_lenses = pygame.font.Font(None, 30)
done_font = pygame.font.Font(None, 100)

color_active = (0, 128, 128)#pygame.Color('lightskyblue3')
color_passive = (180, 200, 210)#pygame.Color('chartreuse4')
indigo = (2,52,63)
skin = (240,237,204)

screen.fill(skin)

done = pygame.Rect(400, 500, 300, 100)
done_text = done_font.render("Done", True, skin)

input_fields = [
    {"label": "Name:", "rect": pygame.Rect(175, 50, 280, 50), "text": "", "active": False},
    {"label": "Year:", "rect": pygame.Rect(175, 125, 280, 50), "text": "", "active": False},
    {"label": "Course:", "rect": pygame.Rect(175, 200, 280, 50), "text": "", "active": False},
    {"label": "Email:", "rect": pygame.Rect(175, 275, 280, 50), "text": "", "active": False},
    {"label": "GCash:", "rect": pygame.Rect(650, 50, 280, 50), "text": "", "active": False},
    {"label": "Sex at Birth:", "rect": pygame.Rect(650, 125, 280, 50), "text": "", "active": False},
    {"label": "Age:", "rect": pygame.Rect(650, 200, 280, 50), "text": "", "active": False},
    {"label": "Wears Corrective Lenses:", "rect": pygame.Rect(650, 275, 280, 50), "text": "", "active": False}
]

run = True

while run:
    #screen.fill((0, 0, 0))  

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

            if done.collidepoint(event.pos):
                data = {}
                file = pd.read_csv("info.csv", header=0)
                for fields in input_fields:
                    data[fields["label"]] = fields["text"]

                    if fields["label"] == "Name:":
                        name = fields["text"]
                    if fields["label"] == "Email:":
                        email = fields["text"]

                unique_id = name + email
                data["unique_id"] = unique_id
                data["score"] = 0

                config_data = {
                    "unique_id" : unique_id
                }

                with open("config.py", "w") as config_file:
                    config_file.write(f"CONFIG = {config_data}")

                new_row = pd.DataFrame([data])
                file = pd.concat([file, new_row], ignore_index = True)
                file.to_csv('info.csv', index = False)

                runpy.run_path("landing page.py")
                run = False

        if event.type == pygame.KEYDOWN:
            for field in input_fields:
                if field["active"]:
                    if event.key == pygame.K_BACKSPACE:
                        field["text"] = field["text"][:-1]
                    else:
                        field["text"] += event.unicode
        


    pygame.draw.rect(screen, indigo, done)
    screen.blit(done_text, (done.x + 60, done.y + 17))

    for field in input_fields:

        pygame.draw.rect(screen, color_active if field["active"] else color_passive, field["rect"])

        if field["label"] == "Sex at Birth:":
            label_width, _ = sex_at_birth.size(field["label"])
            label_x = field["rect"].x - (label_width + 10)

            label_surface = sex_at_birth.render(field["label"], False, indigo)
            screen.blit(label_surface, (label_x, field["rect"].y + 10))

            input_surface = base_font.render(field["text"], True, (255, 255, 255))
            screen.blit(input_surface, (field["rect"].x + 5, field["rect"].y + 10))

            field["rect"].w = max(280, input_surface.get_width() + 10)

        elif field["label"] == "Wears Corrective Lenses:":

            label_width1, _ = corrective_lenses.size("Wears Corrective:")
            label_width2, _ = corrective_lenses.size("Lenses:")
            label_x1 = field["rect"].x - (label_width1 + 5)
            label_x2 = field["rect"].x - (label_width2 + 5)

            label_surface1 = corrective_lenses.render("Wears Corrective", False, indigo)
            label_surface2 = corrective_lenses.render("Lenses:", False, indigo)

            screen.blit(label_surface1, (field["rect"].x - (label_width1 + 5), field["rect"].y + 5))
            screen.blit(label_surface2, (field["rect"].x - (label_width2 + 10), field["rect"].y + 25))

            input_surface = base_font.render(field["text"], True, (255, 255, 255))
            screen.blit(input_surface, (field["rect"].x + 5, field["rect"].y + 10))

            field["rect"].w = max(280, input_surface.get_width() + 10)

        elif field["label"] not in ["Wears Corrective Lenses:", "Sex at Birth:"]:
            label_width, _ = label_font.size(field["label"])
            label_x = field["rect"].x - (label_width + 10)
            
            label_surface = label_font.render(field["label"], False, indigo)
            screen.blit(label_surface, (label_x, field["rect"].y + 5))
            
            input_surface = base_font.render(field["text"], True, (255, 255, 255))
            screen.blit(input_surface, (field["rect"].x + 5, field["rect"].y + 12.5))

            field["rect"].w = max(280, input_surface.get_width() + 10)

    for field in input_fields:
        guide = {
            "Year:" : "e.g. 1st, 2nd, etc.",
            "Course:" : "e.g. BS Statistics",
            "GCash:" : "Optional",
            "Sex at Birth:" : "Male or Female",
            "Wears Corrective Lenses:" : "Yes or No"
        }
        if field["text"] == '' and field["label"] in ('Year:','Course:','GCash:','Sex at Birth:', 'Wears Corrective Lenses:'):

            input_surface = base_font.render(guide[field["label"]], True, skin)
            screen.blit(input_surface, (field["rect"].x + 5, field["rect"].y + 12.5))

    pygame.display.flip()

pygame.quit()


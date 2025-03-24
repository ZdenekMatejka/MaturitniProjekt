import pygame

# Inicializace pygame
pygame.init()

# Vytvoření obrazovky
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maturitní projekt - Hra")

# Definujeme barvy (0 - 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#Systémové fonty
#fonts = pygame.font.get_fonts()
#for one_font in fonts:
#    print(one_font)

# Nastavení fontu
system_font = pygame.font.SysFont("Times New Roman", 64)

# Font a text
system_text = system_font.render("Můj text", True, white, red)
system_text_rect = system_text.get_rect()
system_text_rect.center = (width//2, height//2)

# Barva pozadí
screen.fill(black)

# Tvar
#pygame.draw.rect(screen, white, (200, 100, 100, 100))

# Obrázky
wolf_image = pygame.image.load("img/amarok-wolf-icon.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.topleft = (0, 200)


# Hlavní herní cyklus - vykreslování okna a zavření
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Přidání obrázku
    screen.blit(wolf_image, wolf_rect)

    #Přidání textu
    screen.blit(system_text, system_text_rect)

    # Obnovujeme obrazovku
    pygame.display.update()


# Ukonční pygame
pygame.quit()
import pygame

# Inicializace pygame
pygame.init()

# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Název hry")

# Hlavní herní cyklus - vykreslování okna a zavření
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Obnovujeme obrazovku
    pygame.display.update()

# Ukonční pygame
pygame.quit()
import pygame

# Inicializace pygame
pygame.init()

# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maturitní projekt - Hra")


# Definujeme barvy (0 - 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Barva pozadí
screen.fill(black)

# Tvary
    # čára
pygame.draw.line(screen, white, (0, 0), (width//2, height//2), 3)
    # kružnice
pygame.draw.circle(screen, yellow, (width//2, height//2), 100, 5)
    # kruh
pygame.draw.circle(screen, red, (width//2, height//2), 90, 0)
    # čtverec, obdélník
pygame.draw.rect(screen, blue, (width//2 - 50, height//2 - 50, 100, 120))

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
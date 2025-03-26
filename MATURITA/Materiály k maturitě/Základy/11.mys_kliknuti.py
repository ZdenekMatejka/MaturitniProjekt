import pygame

# Inicializace pygame
pygame.init()

# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maturitní projekt - Hra")

# Základní nastavení
distance = 10
fps = 60
clock = pygame.time.Clock()


# Definujeme barvy (0 - 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Systémové fonty
#fonts = pygame.font.get_fonts()
#for one_font in fonts:
#    print(one_font)

# Nastavení fontu
system_font = pygame.font.SysFont("Times New Roman", 45)
custom_font = pygame.font.Font("fonts/Text.ttf", 30)

# Font a text
system_text = system_font.render("Můj text", True, white)
system_text_rect = system_text.get_rect()
system_text_rect.midtop = (width//2, 5)

custom_text = custom_font.render("Maturitní hra", True, white, red)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (400, 200)

# Barva pozadí
#screen.fill(black) -> přesunutí až pod pohyby

# Tvar
#pygame.draw.rect(screen, white, (200, 100, 100, 100))

# Obrázky
wolf_image = pygame.image.load("img/amarok-wolf-icon.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.topleft = (0, 200)

# Hudba v pozadí
#pygame.mixer.music.load("media/bg-music.wav")
# Přehrajeme hudbu
#pygame.mixer.music.play(-1, 0.0)
#pygame.time.delay(3000)
#pygame.mixer_music.stop()

# Nahrání zvuku
#sound_boom = pygame.mixer.Sound("media/boom.wav")

# Změna hlasitosti
#sound_boom.set_volume(0.1)

# Přehrání zvuku
#sound_boom.play()
#pygame.time.delay(2000)
# sound2

# Hlavní herní cyklus - vykreslování okna a zavření
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Kliknutí myší
        if event.type == pygame.MOUSEBUTTONDOWN:
           print(f"Pozice X: {event.pos[0]}")
           print(f"Pozice Y: {event.pos[1]}")
           wolf_rect.centerx = event.pos[0]
           wolf_rect.centery = event.pos[1]

    

    # Plynulý pohyb obrázku
        # w - nahoru, s - dolu, a - doleva, d - doprava
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and wolf_rect.top > 0:
        wolf_rect.y -= distance
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and wolf_rect.bottom < height:
        wolf_rect.y += distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and wolf_rect.left > 0:
        wolf_rect.x -= distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and wolf_rect.right < width: 
        wolf_rect.x += distance


        # Vyplnění obrazovky černou barvou
    screen.fill((black))


    # Přidání obrázku
    screen.blit(wolf_image, wolf_rect)

    #Přidání textu
    screen.blit(system_text, system_text_rect)
    screen.blit(custom_text, custom_text_rect)

    # Obnovujeme obrazovku
    pygame.display.update()

    # tikání hodin
    clock.tick(fps)

# Ukonční pygame
pygame.quit()
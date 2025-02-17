import pygame
import random
import sqlite3

# Inicializace hry
pygame.init()

# Výběr postavy
character_selected = None

# Připojení k databázi
conn = sqlite3.connect("high_scores.db")
cursor = conn.cursor()

# Vytvoření tabulky
cursor.execute("""
CREATE TABLE IF NOT EXISTS high_scores (
    id int PRIMARY KEY,
    score int
)
""")
conn.commit()

# Funkce pro načtení nejvyššího skóre z databáze
def load_high_score():
    cursor.execute("SELECT MAX(score) FROM high_scores")
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

# Funkce pro uložení skóre do databáze
def save_high_score(score):
    cursor.execute("INSERT INTO high_scores (score) VALUES (?)", (score,))
    conn.commit()

def reset_high_score():
    cursor.execute("DELETE FROM high_scores")
    conn.commit()

# Hlavní proměnné hry
score = 0
high_score = load_high_score()

# Obrazovka
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maturitní projekt - Hra")

# Nastavení hry
player_start_lives = 1  # MĚNÍME v průběhu hry
player_speed = 5  # Neměníme v průběhu hry
coin_speed = 5  # MĚNÍME v průběhu hry
coin_speed_acceleration = 0.5  # neměníme v průběhu hry
coin_behind_border = 150  # neměníme v průběhu hry
score = 0  # MĚNÍME v průběhu hry

player_lives = player_start_lives
coin_curent_speed = coin_speed

# FPS a hodiny
fps = 60
clock = pygame.time.Clock()

# Barvy
black = (0, 0, 0)
blue = pygame.Color("#049cd8")
yellow = pygame.Color("#fbd000")
red = pygame.Color("#e52521")
green = pygame.Color("#43b047")
white = (255, 255, 255)

# Fonty
mario_font_big = pygame.font.Font("fonts/MarioFont3.ttf", 47)
mario_font_mid = pygame.font.Font("fonts/MarioFont.ttf", 23)
mario_font_mid2 = pygame.font.Font("fonts/MarioFont3.ttf", 25)
mario_font_g = pygame.font.Font("fonts/MarioFont2.ttf", 40)
mario_font_c = pygame.font.Font("fonts/MarioFont2.ttf", 25)
mario_font_button = pygame.font.Font("fonts/MarioFont3.ttf", 13)
mario_font_e = pygame.font.Font("fonts/MarioFont2.ttf", 20)
mario_font_ch = pygame.font.Font("fonts/MarioFont.ttf", 65)
mario_font_cho = pygame.font.Font("fonts/MarioFont3.ttf", 38)

# Text
game_name = mario_font_big.render("SUPER MARIO GAME", True, white)
game_name_rect = game_name.get_rect()
game_name_rect.center = (width//2 + 60, 40)

game_over_text = mario_font_g.render("GAME OVER!", True, red)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (width//2, height//2)

continue_text = mario_font_c.render("Chces Hrat Znovu? Stiskni Libovolnou Klavesu!", True, white)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (width//2, height//2 + 80)

edited_text = mario_font_e.render("Nejvyssi Skore Bylo Vynulovano", True, white)
edited_text_rect = edited_text.get_rect()
edited_text_rect.center = (width - 170, 110)

# Hudba v pozadí a zvuky
pygame.mixer_music.load("media/GroundTheme.mp3")
pygame.mixer.music.play(-1, 0.0)

loss_life_sound = pygame.mixer.Sound("media/loss.wav")
loss_life_sound.set_volume(2)
take_coin_sound = pygame.mixer.Sound("media/pick.wav")
take_coin_sound.set_volume(2)

# Obrázky
background_img = pygame.image.load("img/background.png")

mario_img = pygame.image.load("img/Mario-icon.png")
mario_img_rect = mario_img.get_rect()
mario_img_rect.center = (300, 300)

luigi_img = pygame.image.load("img/Luigi-icon.png")
luigi_img_rect = luigi_img.get_rect()
luigi_img_rect.center = (670, 300)

marioI_img = pygame.image.load("img/MarioI-icon.png")
marioI_img_rect = mario_img.get_rect()
marioI_img_rect.center = (300, 260)

luigiI_img = pygame.image.load("img/LuigiI-icon.png")
luigiI_img_rect = luigi_img.get_rect()
luigiI_img_rect.center = (640, 260)

coin_image = pygame.image.load("img/Coin-icon.png")
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = width + coin_behind_border
coin_image_rect.y = random.randint(110, height - 48)

# Nastavení tlačítka reset
reset_button_rect = pygame.Rect(width - 150, 45, 130, 30)

# Výběr postavičky
choosing_character = True
while choosing_character:
    screen.blit(background_img, (0, 0))

    title_text = mario_font_ch.render("VYBER SI POSTAVICKU", True, white)
    title_rect = title_text.get_rect(center=(width//2, 100))
    screen.blit(title_text, title_rect)

    mario_text = mario_font_cho.render("MARIO", True, red)
    mario_rect = mario_text.get_rect(center=(320, height - 165))
    screen.blit(mario_text, mario_rect)

    luigi_text = mario_font_cho.render("LUIGI", True, green)
    luigi_rect = luigi_text.get_rect(center=(663, height - 165))
    screen.blit(luigi_text, luigi_rect)

    screen.blit(marioI_img, marioI_img_rect)
    screen.blit(luigiI_img, luigiI_img_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if marioI_img_rect.collidepoint(event.pos):
                character_selected = "mario"
                choosing_character = False
            elif luigiI_img_rect.collidepoint(event.pos):
                character_selected = "luigi"
                choosing_character = False

    pygame.display.update()


# Po výběru nastavíme postavičku
character_images = {
    "mario": mario_img,
    "luigi": luigi_img
}

player_image = character_images.get(character_selected)

# Použití vybrané postavy
player_image_rect = player_image.get_rect(center=(55, height//2))

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
            # Kontrola, zda uživatel klikl na tlačítko reset    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button_rect.collidepoint(event.pos):
                reset_high_score()
                high_score = 0

    # Pohyb klávesami
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_image_rect.top > 85:
        player_image_rect.y -= player_speed
    elif keys[pygame.K_DOWN] and player_image_rect.bottom < height:
        player_image_rect.y += player_speed

    # Pohyb mince
    if coin_image_rect.x < 0:  #je za krajem
        player_lives -= 1
        coin_image_rect.x = width + coin_behind_border
        coin_image_rect.y = random.randint(110, height - 48)
        loss_life_sound.play()
    else:  #mince se pohybuje směrem doleva
        coin_image_rect.x -= coin_curent_speed

    # Kontrola kolize
    if player_image_rect.colliderect(coin_image_rect):
        score += 1  #score = score + 1
        coin_curent_speed += coin_speed_acceleration
        coin_image_rect.x = width + coin_behind_border
        coin_image_rect.y = random.randint(60, height - 48)
        take_coin_sound.play()

    # Aktualizace nejvyššího skóre
    if score > high_score:
        high_score = score
        save_high_score(high_score)

    # Znovu vykreslení obrazovky
    screen.blit(background_img, (0, 0))

    # Tvary
    pygame.draw.line(screen, white, (0, 80), (width, 80), 4)

    # Vykreslení tlačítka reset
    pygame.draw.rect(screen, white, reset_button_rect)

    # Nastavení textů
    lives_text = mario_font_mid.render(f"Zivoty: {player_lives}", True, white)
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.right = width - 25
    lives_text_rect.top = 15

    score_text = mario_font_mid.render(f"Skore: {score}", True, white)
    score_text_rect = score_text.get_rect()
    score_text_rect.left = 25
    score_text_rect.top = 15

    high_score_text = mario_font_mid.render(f"Nejvyssi skore: {high_score}", True, white)
    high_score_text_rect = high_score_text.get_rect()
    high_score_text_rect. left = 25
    high_score_text_rect.top = 47


    reset_text = mario_font_button.render("RESET NEJVYSSIHO", True, blue)
    reset_text_rect = reset_text.get_rect()
    reset_text_rect.left = width - 147
    reset_text_rect.top = 48
    reset_text2 = mario_font_button.render("SKORE", True, blue)
    reset_text2_rect = reset_text2.get_rect()
    reset_text2_rect.left = width - 145
    reset_text2_rect.top = 62

    # Texty - vykreslení
    screen.blit(game_name, game_name_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(lives_text, lives_text_rect)
    screen.blit(high_score_text, high_score_text_rect)
    screen.blit(reset_text, reset_text_rect)
    screen.blit(reset_text2, reset_text2_rect)

    # Obrázky
    screen.blit(coin_image, coin_image_rect)
    # Vykreslení vybrané postavičky
    screen.blit(player_image, player_image_rect)

    # Kontrola konce hry
    if player_lives == 0:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(continue_text, continue_text_rect)
        your_best_score_text = mario_font_g.render(f"Tvoje Nejvyssi Skore Je: {high_score}", True, blue)
        your_best_score_text_rect = your_best_score_text.get_rect()
        your_best_score_text_rect.center = (width//2, height//2 + 160)
        screen.blit(your_best_score_text, your_best_score_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        pause = True

        while pause: 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_button_rect.collidepoint(event.pos):
                        score = 0
                        reset_high_score()
                        high_score = 0
                        screen.blit(edited_text, edited_text_rect)
                        pygame.display.update()
                

                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = player_start_lives
                    coin_curent_speed = coin_speed
                    choosing_character = True
                    while choosing_character:
                        screen.blit(background_img, (0, 0))

                        title_text = mario_font_ch.render("VYBER SI POSTAVICKU", True, white)
                        title_rect = title_text.get_rect(center=(width//2, 100))
                        screen.blit(title_text, title_rect)

                        mario_text = mario_font_cho.render("MARIO", True, red)
                        mario_rect = mario_text.get_rect(center=(320, height - 165))
                        screen.blit(mario_text, mario_rect)

                        luigi_text = mario_font_cho.render("LUIGI", True, green)
                        luigi_rect = luigi_text.get_rect(center=(663, height - 165))
                        screen.blit(luigi_text, luigi_rect)

                        screen.blit(marioI_img, marioI_img_rect)
                        screen.blit(luigiI_img, luigiI_img_rect)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if marioI_img_rect.collidepoint(event.pos):
                                    character_selected = "mario"
                                    choosing_character = False
                                elif luigiI_img_rect.collidepoint(event.pos):
                                    character_selected = "luigi"
                                    choosing_character = False

                        pygame.display.update()


                    # Po výběru nastavíme postavičku
                    character_images = {
                        "mario": mario_img,
                        "luigi": luigi_img
                    }

                    player_image = character_images.get(character_selected)

                    # Použití vybrané postavy
                    player_image_rect = player_image.get_rect(center=(55, height//2))
                    pause = False
                    pygame.mixer.music.play(-1, 0.0)
                
                elif event.type == pygame.QUIT:
                    pause = False
                    lets_continue = False
                    

    # Obnovení obrazovky
    pygame.display.update()

    # Zpomalení cyklu - Tikání hodin
    clock.tick(fps)

# Ukončení spojení s databází
conn.close()

# Ukončení hry
pygame.quit()
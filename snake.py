import pygame
import random
import json
import webbrowser

# pygame initialization
pygame.init()

# clock
clock = pygame.time.Clock()

# media
viko = pygame.image.load('viko_logo_new.png')
gameIcon = pygame.image.load('snake.jpeg')
crash_sound = pygame.mixer.Sound("crash.wav")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
sky_blue = (9, 75, 135)

# Create the Screen
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game (First Programing Practice)")
pygame.display.set_icon(gameIcon)

smallText = pygame.font.SysFont("comicsansms", 20)
largeText = pygame.font.SysFont("comicsansms", 115)
message_font = pygame.font.SysFont('freesansbold.ttf', 30)
score_font = pygame.font.SysFont('ubuntu', 25)
snake_size = 10
snake_speed = 15

pause = False


def logo(x, y):
    game_display.blit(viko, (x, y))


def shop():
    webbrowser.open('http://127.0.0.1:8000')


def hs():
    with open('score.json', 'r') as f:
        json_data = json.load(f)
    return int(json_data['high_score'])


def text_objects(text, font, cl):
    textSurface = font.render(text, True, cl)
    return textSurface, textSurface.get_rect()


def text1(word, x, y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True, red)
    return game_display.blit(text, (x, y))


def introme():
    TextSurf, TextRect = text_objects("Liwaa Audi", smallText, orange)
    TextRect.center = (55, 20)
    game_display.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("s040384", smallText, orange)
    TextRect.center = (45, 50)
    game_display.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("First Programming practice", smallText, orange)
    TextRect.center = (130, 80)
    game_display.blit(TextSurf, TextRect)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(textSurf, textRect)


def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, black, [pixel[0], pixel[1], snake_size, snake_size])


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    x = 550
    y = 18
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        logo(x, y)
        introme()
        TextSurf, TextRect = text_objects("Snake Game", largeText, orange)
        TextRect.center = ((width / 2), (height / 2))
        game_display.blit(TextSurf, TextRect)

        button("Play", 350, 420, 100, 50, sky_blue, orange, run_game)
        button("Shop", 350, 470, 100, 50, sky_blue, orange, shop)
        button("Quit", 350, 520, 100, 50, sky_blue, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    TextSurf, TextRect = text_objects("You Crashed", largeText, red)
    TextRect.center = ((width / 2), 100)
    game_display.blit(TextSurf, TextRect)

    TxtSurf, TxtRect = text_objects("High Score: {}".format(hs()), score_font, orange)
    TxtRect.center = ((width / 2), 500)
    game_display.blit(TxtSurf, TxtRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 350, 250, 100, 50, sky_blue, orange, run_game)
        button("Main", 350, 300, 100, 50, sky_blue, orange, game_intro)
        button("Quit", 350, 350, 100, 50, sky_blue, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False


def paused():
    pygame.mixer.music.pause()
    TextSurf, TextRect = text_objects("Paused", largeText, orange)
    TextRect.center = ((width / 2), 100)
    game_display.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 350, 250, 100, 50, sky_blue, orange, unpause)
        button("Main", 350, 300, 100, 50, sky_blue, orange, game_intro)
        button("Quit", 350, 350, 100, 50, sky_blue, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def run_game():
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    global pause
    game_over = False
    game_close = False

    # starting position
    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            crash()
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = True
                    if event.key == pygame.K_2:
                        run_game()

                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0

                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size

                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            x += x_speed
            y += y_speed

            game_display.fill(white)
            pygame.draw.rect(game_display, sky_blue, [food_x, food_y, snake_size, snake_size])

            snake_pixels.append([x, y])

            if len(snake_pixels) > snake_length:
                del snake_pixels[0]

            # snake ran into it self
            for pixel in snake_pixels[:-1]:
                if pixel == [x, y]:
                    game_close = True

            draw_snake(snake_size, snake_pixels)
            print_score(snake_length - 1)
            score = snake_length - 1
            with open('score.json', 'r') as f:
                json_data = json.load(f)
                if score >= int(json_data['high_score']):
                    json_data['high_score'] = str(score)

            with open('score.json', 'w') as f:
                f.write(json.dumps(json_data))

            pygame.display.update()

            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
                food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
                snake_length += 1

            clock.tick(snake_speed)

    pygame.quit()
    quit()


game_intro()
run_game()

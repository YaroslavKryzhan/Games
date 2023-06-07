import pygame
import sys
import random

# Инициализация Pygame и создание окна
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Создание часов Pygame для контроля FPS
clock = pygame.time.Clock()

# Определение свойств ракеток и мяча
paddle_speed = 15
paddle_width = 15
paddle_height = 80
ball_speed = 7
ball_size = 15
paddle1_score = 0
paddle2_score = 0

paddle1 = pygame.Rect(paddle_width, 300, paddle_width, paddle_height)
paddle2 = pygame.Rect(800 - 2*paddle_width, 300, paddle_width, paddle_height)
ball = pygame.Rect(400, 300, ball_size, ball_size)

font = pygame.font.Font(None, 36)

paused = False  # Variable for game pause status

def show_go_screen():
    screen.fill((0, 0, 0))
    draw_text("PONG!", 64, 400, 150)
    draw_text("Player 1: W/S. Player 2: Up/Down", 22, 400, 250)
    draw_text("Press A key to begin, E to exit", 25, 400, 350)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    waiting = False
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

def show_pause_screen():
    global paused
    draw_text("PAUSED", 64, 400, 300)
    draw_text("Press ESC to continue", 22, 400, 350)
    pygame.display.flip()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    paused = False

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def reset_game():
    global paddle1_score, paddle2_score
    paddle1_score = 0
    paddle2_score = 0
    ball.center = (400, 300)
    show_go_screen()

def check_score():
    if paddle1_score >= 10:
        draw_text("Player 1 Wins!", 50, 400, 300)
        pygame.display.flip()
        pygame.time.delay(2000)
        reset_game()
    elif paddle2_score >= 10:
        draw_text("Player 2 Wins!", 50, 400, 300)
        pygame.display.flip()
        pygame.time.delay(2000)
        reset_game()

# Инициализация игры
show_go_screen()
ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                if paused:
                    show_pause_screen()

    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_ip(0, -paddle_speed)
        if keys[pygame.K_s]:
            paddle1.move_ip(0, paddle_speed)
        if keys[pygame.K_UP]:
            paddle2.move_ip(0, -paddle_speed)
        if keys[pygame.K_DOWN]:
            paddle2.move_ip(0, paddle_speed)

        ball.move_ip(ball_dx, ball_dy)

        # Столкновение мяча с ракетками
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_dx *= -1
        # Столкновение мяча с верхней и нижней границами
        elif ball.top < 0 or ball.bottom > 600:
            ball_dy *= -1

        # Условие выигрыша
        elif ball.left < 0:
            paddle2_score += 1
            check_score()
            ball.center = (400, 300)
            ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])
            pygame.time.delay(1000)
        elif ball.right > 800:
            paddle1_score += 1
            check_score()
            ball.center = (400, 300)
            ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])
            pygame.time.delay(1000)

        # Ограничение движения ракеток
        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > 600:
            paddle1.bottom = 600
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > 600:
            paddle2.bottom = 600

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), paddle1)
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.aaline(screen, (255, 255, 255), (400, 0), (400, 600))

        draw_text(str(paddle1_score), 22, 200, 50)
        draw_text(str(paddle2_score), 22, 600, 50)

    pygame.display.flip()
    clock.tick(60)
import pygame
import sys
import random

# Инициализация Pygame и создание окна
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Создание часов Pygame для контроля FPS
clock = pygame.time.Clock()

# Определение свойств ракеток и мяча
paddle_speed = 15
paddle_width = 15
paddle_height = 80
ball_speed = 8
ball_size = 15
paddle1_score = 0
paddle2_score = 0

paddle1 = pygame.Rect(paddle_width, 300, paddle_width, paddle_height)
paddle2 = pygame.Rect(800 - 2*paddle_width, 300, paddle_width, paddle_height)
ball = pygame.Rect(400, 300, ball_size, ball_size)

font = pygame.font.Font(None, 36)

paused = False  # Variable for game pause status

def show_go_screen():
    screen.fill((0, 0, 0))
    draw_text("PONG!", 64, 400, 150)
    draw_text("Player 1: W/S. Player 2: Up/Down", 22, 400, 250)
    draw_text("Press A key to begin, E to exit", 25, 400, 350)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    waiting = False
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

def show_pause_screen():
    global paused
    draw_text("PAUSED", 64, 400, 300)
    draw_text("Press ESC to continue", 22, 400, 350)
    pygame.display.flip()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    paused = False

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def reset_game():
    global paddle1_score, paddle2_score
    paddle1_score = 0
    paddle2_score = 0
    ball.center = (400, 300)
    show_go_screen()

def check_score():
    if paddle1_score >= 10:
        draw_text("Player 1 Wins!", 50, 400, 300)
        pygame.display.flip()
        pygame.time.delay(2000)
        reset_game()
    elif paddle2_score >= 10:
        draw_text("Player 2 Wins!", 50, 400, 300)
        pygame.display.flip()
        pygame.time.delay(2000)
        reset_game()

# Инициализация игры
show_go_screen()
ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                if paused:
                    show_pause_screen()

    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_ip(0, -paddle_speed)
        if keys[pygame.K_s]:
            paddle1.move_ip(0, paddle_speed)
        if keys[pygame.K_UP]:
            paddle2.move_ip(0, -paddle_speed)
        if keys[pygame.K_DOWN]:
            paddle2.move_ip(0, paddle_speed)

        ball.move_ip(ball_dx, ball_dy)

        # Столкновение мяча с ракетками
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_dx *= -1
        # Столкновение мяча с верхней и нижней границами
        elif ball.top < 0 or ball.bottom > 600:
            ball_dy *= -1

        # Условие выигрыша
        elif ball.left < 0:
            paddle2_score += 1
            check_score()
            ball.center = (400, 300)
            ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])
            pygame.time.delay(1000)
        elif ball.right > 800:
            paddle1_score += 1
            check_score()
            ball.center = (400, 300)
            ball_dx, ball_dy = ball_speed * random.choice([-1, 1]), ball_speed * random.choice([-1, 1])
            pygame.time.delay(1000)

        # Ограничение движения ракеток
        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > 600:
            paddle1.bottom = 600
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > 600:
            paddle2.bottom = 600

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), paddle1)
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.aaline(screen, (255, 255, 255), (400, 0), (400, 600))

        draw_text(str(paddle1_score), 22, 200, 50)
        draw_text(str(paddle2_score), 22, 600, 50)

    pygame.display.flip()
    clock.tick(60)

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
paddle1_x = 10
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 10
paddle2_y = height // 2 - paddle_height // 2

# Set up ball
ball_radius = 8
ball_x = width // 2
ball_y = height // 2
ball_speed_x = random.choice([-2, 2])
ball_speed_y = random.choice([-2, 2])

# Set up game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    elif ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Drawing
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

    # Update display
    pygame.display.flip()

    # Set the game's FPS
    clock.tick(60)

# Quit the game
pygame.quit()

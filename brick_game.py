import pygame
import sys
from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick
from brick import create_bricks, check_brick_collision

def run_game():
    pygame.init()
    brick_settings = Settings()
    window = pygame.display.set_mode((brick_settings.SCREEN_WIDTH, brick_settings.SCREEN_HEIGHT))
    window.fill(brick_settings.BG_COLOUR)
    pygame.display.set_caption("brick")
    text = pygame.font.Font(r"Pixeltype.ttf", 36)
    paddle = Paddle(brick_settings, window)

    ball = Ball(brick_settings, window)
    lives = 3
    rows = 1
    score = 0
    bricks = create_bricks(rows)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            paddle.check_events(event, brick_settings)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lives > 0:
                    ball.reset_ball(brick_settings)
                    lives -= 1

        ball.move(brick_settings, paddle)
        score = check_brick_collision(bricks, ball, score)

        # Create new row of bricks
        if not bricks:
            if rows < 5:
                rows += 1
            # Increase ball velocity
            if rows >= 2:
                ball.X_VELOCITY *= 1.1
                ball.Y_VELOCITY *= 1.1
            bricks = create_bricks(rows)

        # Clear window and draw updated paddle.
        window.fill(brick_settings.BG_COLOUR)

        for brick in bricks:
            brick.draw_brick(window)

        paddle.draw_paddle()
        lives_text = text.render(f"Lives: {lives}", False, "grey")
        score_text = text.render(f"Score: {score}", False, "grey")
        window.blit(lives_text, (20, 590))
        window.blit(score_text, (880, 590))
        ball.draw_ball()

        pygame.display.flip()


run_game()
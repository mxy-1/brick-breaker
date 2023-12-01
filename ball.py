import pygame

class Ball():
    def __init__(self, brick_settings, screen):
        self.screen = screen
        self.RADIUS = 15
        self.COLOUR = (160, 165, 160)
        self.X_VELOCITY = 6
        self.Y_VELOCITY = 6
        self.START_X = brick_settings.SCREEN_WIDTH / 2
        self.START_Y = brick_settings.SCREEN_HEIGHT // 3

        # Start point of ball.
        self.x = self.START_X
        self.y = self.START_Y

    def move(self, brick_settings, paddle):
        self.x += self.X_VELOCITY
        self.y += self.Y_VELOCITY

        # Change direction if ball hits top.
        if self.y <= self.RADIUS:
            self.Y_VELOCITY *= -1
        # Change direction if ball hits sides.
        if (self.x + self.RADIUS >= brick_settings.SCREEN_WIDTH) or (self.x <= self.RADIUS):
            self.X_VELOCITY *= -1
        # Change direction if ball hits paddle.
        if (self.y + self.RADIUS >= paddle.rect.topleft[1]) and (self.y <= paddle.rect.midleft[1]) and self.Y_VELOCITY > 0:
            if self.x + self.RADIUS >= paddle.rect.topleft[0] and self.x <= paddle.rect.topright[0] + self.RADIUS:
                self.Y_VELOCITY *= -1
                if self.x + self.RADIUS == paddle.rect.topleft[0] or self.x == paddle.rect.topright[0] + self.RADIUS:
                    self.X_VELOCITY *= -1

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.COLOUR, (self.x, self.y), self.RADIUS)

    # Return ball to starting position.
    def reset_ball(self, brick_settings):
        if self.y - self.RADIUS > brick_settings.SCREEN_HEIGHT:
            self.x = self.START_X
            self.y = self.START_Y


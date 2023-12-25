import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, brick_settings, screen):
        super().__init__()
        self.screen = screen
        self.paddle_width = 180 
        self.paddle_height = 30
        self.colour = (85, 90, 150)
        # Place paddle on specific location.
        self.paddle_mid_x = brick_settings.SCREEN_WIDTH / 2
        self.paddle_mid_y = brick_settings.SCREEN_HEIGHT - 50
        self.rect = pygame.Rect(0, 0, self.paddle_width, self.paddle_height)
        self.rect.midtop = (self.paddle_mid_x, self.paddle_mid_y)

    def check_events(self, event, brick_settings):
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            # Move paddle within screen.
            if (self.rect.x + self.paddle_width / 2 < pos[0]) and self.rect.topright[0] <= brick_settings.SCREEN_WIDTH:
                self.rect.x += 15
            if (self.rect.x + self.paddle_width / 2 > pos[0]) and self.rect.x >= 0:
                self.rect.x -= 15

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def shrink(self):
        self.paddle_width *= 0.5
        self.draw_paddle()
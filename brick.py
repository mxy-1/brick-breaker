import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.WIDTH = 100
        self.HEIGHT = 30
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        self.bricks = []
        self.RED = (220, 70, 80)
        self.ORANGE = (255, 160, 40)
        self.YELLOW = (255, 240, 50)
        self.GREEN = (80, 240, 100)
        self.BLUE = (60, 200, 250)
        self.colours = [self.RED, self.ORANGE, self.YELLOW, self.GREEN, self.BLUE]

    def draw_brick(self, screen):
        # Rows of bricks and colours
        if self.y == 10:
            i = 0
        if self.y == 50:
            i = 1
        if self.y == 90:
            i = 2
        if self.y == 130:
            i = 3
        if self.y >= 170:
            i = 4
        pygame.draw.rect(screen, self.colours[i], self.rect)


def create_bricks(rows):
    GAP = 10
    x = 10
    y = 10
    bricks = []
    for _ in range(rows):
        for _ in range(9):
            brick = Brick(x, y)
            bricks.append(brick)
            x = x + brick.WIDTH + GAP
        x = 10
        y = y + GAP + brick.HEIGHT
    return bricks


def check_brick_collision(bricks, ball):
    for brick in bricks.copy():
        if (ball.x + ball.RADIUS >= brick.rect.topleft[0]) and (ball.x <= brick.rect.topright[0] + ball.RADIUS) \
                and (ball.y + ball.RADIUS >= brick.y) and (ball.y - ball.RADIUS <= brick.y):
            bricks.remove(brick)
            if ball.Y_VELOCITY < 0:
                ball.Y_VELOCITY *= -1

def update_score(score):
    score += 1
    return score

def new_bricks(bricks):
    if not bricks:
        create_bricks()

def update_bricks():
    x = 10
    y = 10
    bricks = []
    rows = 1

    if len(bricks) == 0:
        for _ in range(rows):
            for _ in range(9):
                bricks.append(Brick(x, y))
                x += 110
                if not bricks:
                    rows += 1
            y += 50
    return bricks



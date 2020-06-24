import pygame
from settings import *
from pygame import Vector2

class Pad(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((PAD_WIDTH, PAD_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.velocity = Vector2(0, 0)

    def update(self):
        keystate = pygame.key.get_pressed()
        dx = 0
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            dx = -1
        elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            dx = +1
        self.move(dx)

    def move(self, dx):
        self.velocity += Vector2(PAD_ACCELERATION * dx, 0) * self.game.dt
        self.rect.center += self.velocity * self.game.dt

        # Limits position to screen coordinates
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity = Vector2(0,0)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.velocity = Vector2(0,0)

        # Limits velocity max speed and rounds to zero fast when negative
        self.velocity -= self.velocity * DRAG * self.game.dt
        if self.velocity.magnitude() > PAD_MAX_SPEED:
            self.velocity.scale_to_length(PAD_MAX_SPEED)
        if self.velocity.magnitude() < 25:
            self.velocity = Vector2(0,0)

    def hit_ball(self, ball):
        ball.rect.bottom = self.rect.top 
        ball.velocity.y *= -1
        offset = 2 * (ball.rect.centerx - self.rect.centerx) / PAD_WIDTH
        ball.velocity.x = offset


class Ball(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((BALL_RADIUS, BALL_RADIUS))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        # self.speed = BALL_SPEED
        self.velocity = Vector2(0, 0)
        self.asleep = True
        

    def update(self):
        if self.asleep:
            if self.game.player.velocity.magnitude() > 0:
                self.asleep = False
                self.velocity = self.game.player.velocity.normalize() - Vector2(0, 1)
            return
        if self.velocity.magnitude() > 0:
            self.rect.center += self.velocity.normalize() * BALL_SPEED * self.game.dt

        # Ball rebound with the walls
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x *= -1
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.velocity.x *= -1
        elif self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y *= -1

        # Ball lost
        if self.rect.bottom > HEIGHT:
            self.game.ball_lost()
            self.kill()


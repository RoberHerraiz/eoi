import random

import pygame
from settings import *
from pygame import Vector2

class Pad (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.pad_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.hitbox = self.rect
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.half_pad_width = self.rect.width/2

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
        self.position += self.velocity * self.game.dt

        # Limits position to screen coordinates
        if self.position.x < self.half_pad_width:
            self.position.x = self.half_pad_width
            self.velocity = Vector2(0,0)

        if self.position.x > WIDTH-self.half_pad_width:
            self.position.x = WIDTH-self.half_pad_width
            self.velocity = Vector2(0,0)

        # Limits velocity max speed and rounds to zero fast when negative
        self.velocity -= Vector2(self.velocity.x * DRAG * self.game.dt, 0)
        if self.velocity.magnitude() > PAD_MAX_SPEED:
            self.velocity.scale_to_length(PAD_MAX_SPEED)

        self.rect.center = self.position
        v = abs(self.velocity.x * self.game.dt)
        self.hitbox = self.rect.inflate(v, 0)

    def hit_ball(self, ball):
        if ball.position.y < self.position.y:
            offset =  (ball.position.x - self.position.x) / \
                    (self.half_pad_width)
            ball.velocity.x += offset
            ball.position.y = self.position.y - self.hitbox.height / 2 - ball.hitbox.height / 2
            ball.velocity.y *= -1
            ball.push = 200
            self.game.bounce_fx.play()


class Ball (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.ball_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.hitbox = self.rect
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.push = 0
        self.asleep = True
        
    def update(self):
        if self.asleep:
            if self.game.player.velocity.magnitude() > 0:
                self.asleep = False
                self.velocity = self.game.player.velocity.normalize() - Vector2(0, -1)
            return

        if self.velocity.magnitude() > 0:
            self.position += self.velocity.normalize() * (BALL_SPEED + self.push) * self.game.dt

        self.push *= 0.8

        ball_radius = self.rect.size[0] / 2
        # Ball rebound with the walls
        if self.position.x < ball_radius:
            self.position.x = ball_radius
            self.velocity.x *= -1

        if self.position.x > WIDTH - ball_radius:
            self.position.x = WIDTH - ball_radius
            self.velocity.x *= -1

        if self.position.y < ball_radius:
            self.position.y = ball_radius
            self.velocity.y *= -1

        self.rect.center = self.position
        v = BALL_SPEED * self.game.dt
        self.hitbox = self.rect.inflate(v, v)

        # Ball lost
        if self.position.y > HEIGHT + ball_radius:
            self.kill()
            self.game.ball_lost()



    def bounce(self, thing):
        # if fireball \ return

        total_width = (self.hitbox.width + thing.hitbox.width) / 2
        total_height = (self.hitbox.height+ thing.hitbox.height) / 2
        towards_thing = thing.position - self.position
        offset_x = abs(towards_thing.x / total_width)
        offset_y = abs(towards_thing.y / total_height)

        offset = Vector2(offset_x, offset_y)

        is_vertical_bounce = offset_x < offset_y

        if is_vertical_bounce:
            if self.velocity.y > 0:
                self.position.y = thing.position.y - total_height
            else:
                self.position.y = thing.position.y + total_height
            self.velocity.y *= -1
            
        else:
            if self.velocity.x > 0:
                self.position.x = thing.position.x - total_width
            else:
                self.position.x = thing.position.x + total_width
            self.velocity.x *= -1
  
        self.push = 100

class Brick (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.bricks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = random.choice(game.brick_images)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x,y)
        self.hitbox = self.rect
        self.position = Vector2(x,y)

    def hit(self):
        self.game.break_fx.play()
        self.kill()
        self.game.random_powerup(self.position.x, self.position.y)

        
class Multiple_powerup (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.powerups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.multiple_ball_powerup_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.hitbox = self.rect
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.asleep = True

    def hit(self):
        self.game.break_fx.play()
        self.kill()
        self.game.multiple_ball_powerup()

    def update(self):
        self.velocity += Vector2(0, 200) * self.game.dt
        self.position += self.velocity * self.game.dt
        self.rect.center = self.position
        v = abs(self.velocity.x * self.game.dt)
        self.hitbox = self.rect.inflate(v, 0)
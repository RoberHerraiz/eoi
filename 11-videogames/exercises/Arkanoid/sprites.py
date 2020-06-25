import random

import pygame
from settings import *
from pygame import Vector2

class Pad (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((PAD_WIDTH, PAD_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.position = Vector2(x, y)
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
        self.position += self.velocity * self.game.dt
        self.rect.center = self.position

        # Limits position to screen coordinates
        if self.position.x < PAD_WIDTH/2:
            self.position.x = PAD_WIDTH/2
            self.velocity = Vector2(0,0)
        if self.position.x > WIDTH-PAD_WIDTH/2:
            self.position.x = WIDTH-PAD_WIDTH/2
            self.velocity = Vector2(0,0)

        # Limits velocity max speed and rounds to zero fast when negative
        self.velocity -= self.velocity * DRAG * self.game.dt
        if self.velocity.magnitude() > PAD_MAX_SPEED:
            self.velocity.scale_to_length(PAD_MAX_SPEED)


    def hit_ball(self, ball):
        is_vertical_bounce = ball.bounce(self, self.velocity.x)
        offset =  (ball.position.x - self.position.x) / (PAD_WIDTH/2 + BALL_RADIUS/2)
        ball.velocity.x += offset


class Ball (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((BALL_RADIUS, BALL_RADIUS))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.position = Vector2(x, y)
        self.rect.center = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.asleep = True
        

    def update(self):
        if self.asleep:
            if self.game.player.velocity.magnitude() > 0:
                self.asleep = False
                self.velocity = self.game.player.velocity.normalize() - Vector2(0, 1)
            return


        if self.velocity.magnitude() > 0:
            self.position += self.velocity.normalize() * BALL_SPEED * self.game.dt
            self.rect.center = self.position

        # Ball rebound with the walls
        if self.position.x < BALL_RADIUS:
            self.position.x = BALL_RADIUS
            self.posititon = self.rect.center
            self.velocity.x *= -1
        if self.position.x > WIDTH:
            self.position.x = WIDTH - BALL_RADIUS
            self.posititon = WIDTH - BALL_RADIUS
            self.velocity.x *= -1
        if self.position.x < BALL_RADIUS:
            self.position.x = BALL_RADIUS
            self.posititon = self.rect.center
            self.velocity.y *= -1

        # Ball lost
        if self.position.y > HEIGHT + BALL_RADIUS:
            self.game.ball_lost()
            self.kill()


    def bounce(self, thing, thing_velocity_x):
        towards_thing = thing.position - self.position
        # 0..1 0, centro de la cosa, 1, extremo horizontal de la cosa
        offset_x = abs(towards_thing.x /
                         (self.rect.width/2 + thing.rect.width/2))
        offset_y = abs(towards_thing.y /
                         (self.rect.height/2 + thing.rect.height/2))

        is_vertical_bounce = offset_y > offset_x


        total_height = thing.rect.height / 2 - self.rect.height/2
        total_width = thing.rect.width / 2 - self.rect.width/2

        if is_vertical_bounce:
            if self.velocity.y > 0:
                self.position.y = thing.position.y - total_height
            else:
                self.rect.top = thing.position.y + total_height
            self.velocity.y *= -1
            
        else:
            if self.velocity.x > 0:
                self.position.x = thing.position.x - total_width - \
                     abs(thing_velocity_x) * self.game.dt
            else:
                self.position.x = thing.position.x + total_width +\
                     abs(thing_velocity_x) * self.game.dt
            self.velocity.x *= -1
        
        self.posititon = self.rect.center
            

        return is_vertical_bounce



class Brick (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bricks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE]
        self.image.fill(random.choice(colors))
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x,y)
        self.posotion = Vector2(x,y)

    def hit(self):
        self.kill()
        


from settings import *
import pygame
from pygame import Vector2
from random import uniform

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, game, position):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect() 
        self.position = position * TILESIZE
        self.desired_velocity = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def update(self):
        self.handle_input()

        self.velocity -= self.velocity * DRAG * self.game.dt
        self.velocity += self.desired_velocity * PLAYER_ACCELERATION * self.game.dt
        if self.velocity.magnitude() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

        self.position += self.velocity * self.game.dt

        self.rect.x = self.position.x
        self.collide_with_walls('x')
        self.rect.y = self.position.y
        self.collide_with_walls('y')

    def handle_input(self):
        vx, vy = 0 , 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            vx = -1
        if key[pygame.K_d]:
            vx = 1
        if key[pygame.K_w]:
            vy = -1
        if key[pygame.K_s]:
            vy = 1

        self.desired_velocity = Vector2(vx, vy)
        if self.desired_velocity.magnitude() > 0:
            self.desired_velocity = self.desired_velocity.normalize() # para movernos bien en diagonal

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if len(hits) == 0:
            return
        
        if dir == 'x':
            if self.velocity.x > 0:
                self.position.x = hits[0].rect.left - self.rect.width
            if self.velocity.x < 0:
                self.position.x = hits[0].rect.right
            self.velocity.x = 0
            self.rect.x = self.position.x

        if dir == 'y':
            if self.velocity.y > 0:
                self.position.y = hits[0].rect.top - self.rect.height
            if self.velocity.y < 0:
                self.position.y = hits[0].rect.bottom
            self.velocity.y = 0
            self.rect.y = self.position.y


class Mob(pygame.sprite.Sprite):
    def __init__(self, game, groups, position, max_speed,
                   acceleration, max_health, color):

        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.max_speed = max_speed + uniform(-max_speed * 0.25 , max_speed *  0.25)
        self.acceleration = acceleration
        self.position = position * TILESIZE
        self.desired_velocity = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.max_health = max_health
        self.health = max_health

    def update(self):
        pass

    def move(self):
        if self.desired_velocity.magnitude() > 0:
            self.desired_velocity = self.desired_velocity.normalize()

        self.velocity -= self.velocity * DRAG * self.game.dt
        self.velocity += self.desired_velocity * self.acceleration * self.game.dt
        if self.velocity.magnitude() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.position += self.velocity * self.game.dt

        self.rect.x = self.position.x
        self.collide_with_walls('x')
        self.rect.y = self.position.y
        self.collide_with_walls('y')

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if len(hits) == 0:
            return
        
        if dir == 'x':
            if self.velocity.x > 0:
                self.position.x = hits[0].rect.left - self.rect.width
            if self.velocity.x < 0:
                self.position.x = hits[0].rect.right
            self.velocity.x = 0
            self.rect.x = self.position.x

        if dir == 'y':
            if self.velocity.y > 0:
                self.position.y = hits[0].rect.top - self.rect.height
            if self.velocity.y < 0:
                self.position.y = hits[0].rect.bottom
            self.velocity.y = 0
            self.rect.y = self.position.y

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.kill()

    def draw_health(self):
        health = self.health / self.max_health
        bar_width = int(health * self.rect.width)
        health_bar = pygame.Rect(self.position.x, self.position.y - 7, bar_width, 5)
        pygame.draw.rect(self.game.screen, GREEN, health_bar)

class Player(Mob):
    def __init__(self, game, position, max_speed, 
                 acceleration, max_health, color):

        super().__init__(game, game.all_sprites, position,
                         max_speed, acceleration, max_health, color)

        self.max_speed = max_speed 
        self.last_shot_time = 0

    def update(self):
        self.handle_input()
        self.move()
        
    def handle_input(self):
        vx, vy = 0 , 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            vx = -1
        if key[pygame.K_d]:
            vx = 1
        if key[pygame.K_w]:
            vy = -1
        if key[pygame.K_s]:
            vy = 1

        self.desired_velocity = Vector2(vx, vy)

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            x, y  = pygame.mouse.get_pos()
            self.shoot_at(x, y)
    
    def shoot_at(self, x, y):
        time_since_last_shot = pygame.time.get_ticks() - self.last_shot_time
        if time_since_last_shot < GUN_FIRING_RATE:
            return
        bullet_velocity =  Vector2(x, y) - self.position
        if bullet_velocity.magnitude() > 0:
            bullet_velocity = bullet_velocity.normalize()

        Bullet(
            self.game,
            Vector2(self.rect.center),
            bullet_velocity,
            GUN_SPREAD,
            GUN_TTL,
            GUN_SPEED,
            GUN_DAMAGE,
            GUN_COLOR,
            GUN_SIZE
        )

        self.last_shot_time = pygame.time.get_ticks()

class Bee(Mob):
    def __init__(self, game, position, max_speed, 
                 acceleration, max_health, damage, color):

        super().__init__(game, (game.all_sprites, game.mobs),
         position, max_speed, acceleration, max_health, color)

        self.damage = damage
    
    def update(self):
        towards_player = self.game.player.position - self.position
        self.desired_velocity = towards_player
        self.move()
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.player.receive_damage(self.damage * self.game.dt)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, position, velocity,
                 spread, ttl, speed, damage, color, size):

        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.position = position
        self.rect.center = self.position       

        self.ttl = ttl
        self.spawn_time = pygame.time.get_ticks()
        self.speed = speed
        self.damage = damage
        self.velocity = velocity + Vector2(
            uniform(-spread, spread), uniform(-spread, spread))
        self.velocity = self.velocity.normalize()

    def update(self):
        self.position += self.velocity * self.speed * self.game.dt
        self.rect.center = self.position 

        life_time = pygame.time.get_ticks() - self.spawn_time

        if life_time > self.ttl:
            self.kill()

        if pygame.sprite.spritecollide(self, self.game.walls, False):
            self.kill()

        hits = pygame.sprite.spritecollide(self, self.game.mobs, False)
        if len(hits) > 0:
            hits[0].receive_damage(self.damage)
            self.kill()
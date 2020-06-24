import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.playing = False

    def start_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.player = Pad(self, WIDTH // 2, HEIGHT - 64)
        self.ball = Ball(self, WIDTH // 2, HEIGHT - 128)
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.all_sprites.update()

        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        for ball in hits:
            self.player.hit_ball(ball)


    def ball_lost(self):
        self.player.velocity = Vector2(0,0)
        Ball(self, self.player.rect.centerx, self.player.rect.top - 32)

    def draw(self):
        self.screen.fill(DARKBLUE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


game = Game()
game.start_game()
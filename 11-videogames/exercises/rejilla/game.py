import pygame

from settings import *
from sprites import Player


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        for _ in range(32):
            Player(self, 10, 10)


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()


    def setup(self):
        pass


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        self.all_sprites.update()


    def draw(self):

        self.screen.fill(DARKGREY)
        
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))  

        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y)) 

        self.all_sprites.draw(self.screen)

        pygame.display.flip() # para mostrar lo dibujado


game = Game()
game.run()


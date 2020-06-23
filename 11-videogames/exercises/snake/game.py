import pygame

from settings import *
from sprites import Player, Fruit


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        self.font = pygame.font.SysFont("arial", 24)

        self.reset()
        

    def reset(self):
        self.all_sprites.empty()
        self.fruits.empty()
        self.player = Player(self, 10, 10)
        self.fruit = Fruit(self)
        self.score = 0


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
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

        hits = pygame.sprite.spritecollide(
            self.player, self.fruits, False)

        for fruit in hits:
            self.player.grow()
            fruit.teleport()
            self.score += 1

        if not self.player.alive:
            self.reset()

    def draw(self):

        self.screen.fill(BLACK)
        
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))  

        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y)) 

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip() # para mostrar lo dibujado


game = Game()
game.run()


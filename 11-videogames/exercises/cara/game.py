import pygame

from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        pass 

    def draw(self):
        
        # cara
        pygame.draw.circle(self.screen, YELLOW, (WIDTH//2, HEIGHT//2), 150)

        # ojos
        pygame.draw.circle(self.screen, BLACK, (WIDTH//2+50, HEIGHT//2-60), 15) # DERECHO
        pygame.draw.circle(self.screen, BLACK, (WIDTH//2-50, HEIGHT//2-60), 15) # IZQUIERDO

        # nariz
        # pygame.draw.rect(self.screen, WHITE, [WIDTH//2-50, HEIGHT//2, 100, 100])
        # pygame.draw.arc(self.screen, WHITE, pygame.rect(270, 200, 100, 50), 0 , radians(180)

        # boca
        pygame.draw.circle(self.screen, BLACK, (WIDTH//2, HEIGHT//2+60), 60)

        pygame.display.flip() # para mostrar lo dibujado


game = Game()
game.run()


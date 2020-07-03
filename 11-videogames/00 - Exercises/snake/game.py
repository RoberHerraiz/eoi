import pygame

from settings import *
from sprites import Player, Fruit


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HEIGHT])

        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont("arial", 32)
        

    def start_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        self.player = Player(self, 10, 10)
        self.fruit = Fruit(self)

        self.score = 0
        self.run()


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.event()
            self.update()
            self.draw()
        self.game_over()


    def setup(self):
        pass


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.grow()


    def update(self):
        self.all_sprites.update()

        hits = pygame.sprite.spritecollide(
            self.player, self.fruits, False)

        for fruit in hits:
            self.player.grow()
            fruit.teleport()
            self.score += 1

        self.playing = self.player.alive



    def draw(self):

        self.screen.fill(BLACK)
        
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))  

        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y)) 

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        score_text = self.small_font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip() # para mostrar lo dibujado


    #
    #   MENU
    #

    def main_menu(self):
        title_text = self.large_font.render('SNAKE', True, YELLOW)
        instructions_text = self.small_font.render("Press any key to START", True, WHITE)

        self.screen.fill(DARKGREY)
        self.screen.blit(title_text,
                        (WIDTH // 2 - title_text.get_rect().width // 2,
                        HEIGHT // 2  - title_text.get_rect().height // 2))

        self.screen.blit(instructions_text,
                        (WIDTH // 2 - instructions_text.get_rect().width // 2,
                        HEIGHT - 64))


        pygame.display.flip()
        pygame.time.delay(1000)

        in_main_menu = True

        while in_main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
                    self.start_game()


    def game_over(self):
        title_text = self.large_font.render('GAME OVER', True, YELLOW)
        score_text = self.small_font.render(
            f"Score: {self.score} [Press any key]", True, WHITE)

        self.screen.fill(DARKGREY)
        self.screen.blit(title_text,
                        (WIDTH // 2 - title_text.get_rect().width // 2,
                        HEIGHT // 2  - title_text.get_rect().height // 2))

        self.screen.blit(score_text,
                        (WIDTH // 2 - score_text.get_rect().width // 2,
                        HEIGHT - 64))


        pygame.display.flip()
        pygame.time.delay(1000)

        in_game_over = True

        while in_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_game_over = False
                    self.main_menu()




game = Game()
game.main_menu()


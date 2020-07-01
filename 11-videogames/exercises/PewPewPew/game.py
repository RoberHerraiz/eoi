import pygame
from settings import *
from sprites import *
from map import Map

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont("arial", 32)

        self.playing = False
        self.load_data()

        

    def load_data(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()

        self.map = Map()
        self.map.load_from_file('map.txt')
        self.map.create_sprites_from_map_data(self)

        self.player = Player(
            self, 
            self.map.player_entry_point,
            PLAYER_MAX_SPEED,
            PLAYER_ACCELERATION,
            PLAYER_HEALTH,
            YELLOW
        )
    
    def start_game(self):
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


    def draw(self):
        self.screen.fill(DARKGREEN)
        self.all_sprites.draw(self.screen)

        for mob in self.mobs:
            mob.draw_health()

        self.draw_game_ui()

        pygame.display.flip()
    
    def draw_game_ui(self):
        # health_text = self.small_font.render('Health:', True, BLUE)
        # self.screen.blit(health_text, (10, 10))

        health = self.player.health / self.player.max_health
        padding = 3
        width = 100
        height = 25

        health_background = pygame.Rect(5, 5, width, height)
        bar_width = int(health * (width - padding*2))
        health_fill = pygame.Rect(
        5 + padding, 5 + padding, bar_width, height - padding*2)
        pygame.draw.rect(self.screen, DARKBLUE, health_background)
        pygame.draw.rect(self.screen, BLUE, health_fill)





game = Game()
game.start_game()
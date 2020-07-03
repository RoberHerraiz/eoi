from os import path

import pygame

from settings import *
from sprites import *



class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2,1024)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        pygame.display.set_caption(GAME_TITLE)
        
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont("arial", 32)

        self.load_data()
        self.main_menu()

    def load_data(self):
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "img")
        self.fx_folder = path.join(root_folder, "sound")

        # Load images
        brick_colors = ['blue', 'green', 'grey', 'purple', 'red', 'yellow']
        self.brick_images = []
        for color in brick_colors:
            img = pygame.image.load(
                path.join(img_folder, f'element_{color}_rectangle.png')).convert_alpha()
            self.brick_images.append(img)

        self.ball_image = pygame.image.load(
            path.join(img_folder, 'ballBlue.png')).convert_alpha()

        self.pad_image = pygame.image.load(
            path.join(img_folder, 'paddleBlu.png')).convert_alpha()

        self.multiple_ball_powerup_image = pygame.image.load(
            path.join(img_folder, 'element_blue_diamond.png')).convert_alpha()
        

        # Load FX
        self.bounce_fx = pygame.mixer.Sound(path.join(self.fx_folder, 'bounce.wav'))
        self.break_fx = pygame.mixer.Sound(path.join(self.fx_folder, 'break.wav'))
        self.game_over_fx = pygame.mixer.Sound(path.join(self.fx_folder, 'game_over.ogg'))

    def start_game(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(path.join(self.fx_folder, 'Adventure.mp3'))
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.player = Pad(self, WIDTH // 2, HEIGHT - 64)
        self.ball = Ball(self, WIDTH // 2, HEIGHT - 128)
        self.build_brick_wall()
        self.score = 0
        self.lives = 3
        self.run()
        

    def build_brick_wall(self):
        brick_width = self.brick_images[0].get_rect().width
        brick_height = self.brick_images[0].get_rect().height
        for x in range (8):
            for y in range(7):
                brick_x = 90 + brick_width * x + 2*x
                brick_y = 50 + brick_height * y + 2*y
                Brick(self, brick_x, brick_y)
    
    def run(self):
        self.playing = True
        pygame.mixer.music.play()  
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.multiple_ball_powerup()
                    

    def update(self):
        self.all_sprites.update()
        self.update_collisions()

    def hitbox_collide(self, sprite, other):
        return sprite.hitbox.colliderect(other.hitbox)

    def update_collisions(self):
        hits = pygame.sprite.spritecollide(
            self.player, self.balls, False, self.hitbox_collide)
        for ball in hits:
            self.player.hit_ball(ball)

        brick_hits = pygame.sprite.groupcollide(
            self.balls, self.bricks, False, False, self.hitbox_collide)

        #hits .> [(ball,[brick, brick1, brick2]), (ball2, [brick2])...]
        for ball, bricks in brick_hits.items():
            the_brick = bricks[0]
            ball.bounce(the_brick)
            the_brick.hit()
            self.score += 10

        powerup_hits = pygame.sprite.spritecollide(
            self.player, self.powerups, True, self.hitbox_collide)
        for _ in powerup_hits:
            self.powerup.hit()

    def random_powerup(self, x, y):
        spawn_list = ['nothing', 'multiple_balls']
        weights = [90, 95]
        random_spawn = random.choices(spawn_list, cum_weights=weights)
        if random_spawn[0] == 'multiple_balls':
            self.powerup = Multiple_powerup(self, x, y)

    def multiple_ball_powerup(self):
        if len(self.balls.sprites()) == 0:
            return
        
        reference = self.balls.sprites()[0]
        if reference.asleep:
            return

        for _ in range(MULTIBALL_POWERUP):
            ball = Ball(self, reference.position.x, reference.position.y)
            ball.velocity = Vector2(
                reference.velocity.x * random.uniform(-0.5, 0.5), 
                reference.velocity.x * random.uniform(0.75, 1.25))
   
            ball.asleep = False


    def ball_lost(self):
        if len(self.balls.sprites()) == 0:
            self.player.velocity = Vector2(0,0)
            self.ball = Ball(self, self.player.rect.centerx,
                             self.player.rect.top - 32)
            self.in_game_balls = 1
            self.lives -= 1
        if self.lives <= 0:
            self.game_over()


    def draw(self):
        self.screen.fill(DARKBLUE)
        self.all_sprites.draw(self.screen)

        # Lives
        lives_text = self.small_font.render(f'Lives:  {self.lives}', True, WHITE)
        self.screen.blit(lives_text, (WIDTH - 165, HEIGHT - 75))

        # Score
        score_text = self.small_font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (WIDTH - 165, HEIGHT - 45))

        # dibujar vidas y puntuación

        # # DEBUG
        # for sprite in self.all_sprites:
        #     pygame.draw.rect(self.screen, (0, 230, 0), sprite.rect, 2)
        #     pygame.draw.rect(self.screen, (250, 30, 0), sprite.hitbox, 2)

        pygame.display.flip()


    #
    # MENU
    #


    def main_menu(self):
        title_text = self.large_font.render('ARKANOID', True, YELLOW)
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
                    pygame.time.delay(500)


    def game_over(self):
        pygame.mixer.music.stop()
        self.game_over_fx.play()
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
game.start_game()
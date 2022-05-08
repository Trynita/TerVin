import pygame
from Data.Map.map import Map_manager
import Data.Settings.Data.data as data
import Data.Settings.settings as settings
from Characters.Player.player import Player
from lib.Dialog.dialog import DialogBox


class Game:

    def __init__(self):
        # Démarrage
        self.running = True
        self.map = "world"

        # Affichage de la fenêtre
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((settings.DISPLAY_X, settings.DISPLAY_Y))

        pygame.display.set_caption(data.GAMENAME)

        self.player = Player()
        self.map_manager = Map_manager(self.screen, self.player)
        self.dialog_box = DialogBox()

        # Définir le logo du jeu
        # pygame.display.set_icon(self.player.get())



    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        if pressed[pygame.K_UP]:
            self.player.move_up()
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()



    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()

        # Clock
        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collision(self.dialog_box)

            clock.tick(settings.FPS)

        pygame.quit()

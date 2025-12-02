import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, start_pos):
        super().__init__()

        #find the project on disk
        project_folder = os.path.dirname(__file__)
        #find the sprites
        self.sprite_folder = os.path.join(project_folder, "Sprite pngs")
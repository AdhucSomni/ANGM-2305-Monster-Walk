import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, start_pos):
        super().__init__()

        #find the project on disk
        project_folder = os.path.dirname(__file__)
        #find the sprites
        self.sprite_folder = os.path.join(project_folder, "Sprite pngs")

        #movement
        self.move_left = False
        self.move_right = False
        self.facing_left = False

        #pulling the 'frames/pngs' and forming the walking cycle stages
        self._load_frames()
        self.current_frame_index = 0
        self.last_frame_time = 0
        self.state = "idle" 
        self.walk_frame_delay = 100

        #adding what image to display and collison 
        self.image = self.idle_frames_right[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = start_pos

        #movement
        self.speed = 300
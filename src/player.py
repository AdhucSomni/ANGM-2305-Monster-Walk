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

    def load_frames(self):
        ''' loads all the pngs directly'''

        def load_img(name):
            path = os.path.join(self.sprite_folder, name)
            return pygame.image.load(path).convert_alpha()
        
        #idle frame
        idle_right = load_img("S1.png")
        idle_left = pygame.transform.flip(idle_right, True, False)

        #right facing walk frames
        walk_r1 = load_img("S2.png")
        walk_r2 = load_img("S3.png")

        #left facing walk frames
        walk_l1 = load_img("S4.png")
        walk_l2 = load_img("S5.png")

        self.idle_frames_right = [idle_right]
        self.idle_frames_left = [idle_left]

        self.walk_frames_right = [walk_r1, walk_r2]
        self.walk_frames_left = [walk_l1, walk_l2]
    
    def update_state(self):
        if self.move_left and not self.move_right:
            self.state = "move_left"
            self.facing_left = True
        elif self.move_right and not self.move_left:
            self.state = "move_right"
            self.facing_left = False
        else:
            self.state = "idle"

    def update_animation(self):
        now = pygame.time.get_ticks()

        if self.state == "idle":
            if self.facing_left:
                self.image = self.idle_frames_left[0]
            else:
                self.image = self.idle_frames_right[0]
            self.current_frame_index = 0

        else:
            if now - self.last_frame_time > self.walk_frame_delay:
                self.last_frame_time = now
                self.current_frame_index = (self.current_frame_index + 1) % 2

            if self.state == "move left":
                self.image = self.walk_frames_left[self.current_frame_index]
            else:
                self.image = self.walk_frames_right[self.current_frame_index]
    
    def update(self, dt, screen_width):
        self.update_state()

        velocity_x = 0
        if self.state == "move_left":
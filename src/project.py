import pygame
import sys

def main():
    pygame.init()

    info = pygame.display.Info()
    screen_w, screen_h = info.current_w, info.current_h

    screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Monster-Walk")

    clock = pygame.time.Clock()
    fps = 60

    class Camera:

        def __init__(self):
            self.offset_x = 0

        def follow(self, rect):
            self.offset_x = rect.centerx - screen_w // 2

    class Player(pygame.sprite.Sprite):

        def __init__(self, start_pos):
            super().__init__()

            self.sprite_folder = "Sprite pngs"

            self.move_left = False
            self.move_right = False
            self.facing_left = False

            self.load_frames()

            self.current_frame = 0
            self.last_frame_time = 0
            self.frame_delay = 120
            self.state = "idle"

            self.image = self.idle_right[0]
            self.rect = self.image.get_rect()
            self.rect.midbottom = start_pos
            self.speed = 250

        def load_frames(self):

            def load(name):
                return pygame.image.load(f"{self.sprite_folder}/{name}").convert_alpha()
            
            idle = load("S1.png")
            self.idle_right = [idle]
            self.idle_left = [pygame.transform.flip(idle, True, False)]

            #right facing walk frames
            walk_r1 = load("S2.png")
            walk_r2 = load("S3.png")

            #left facing walk frames
            walk_l1 = load("S4.png")
            walk_l2 = load("S5.png")

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
                self.current_frame_index = 0
                if self.facing_left:
                    self.image = self.idle_left[0]
                else:
                    self.image = self.idle_right[0]
            else:
                if now - self.last_frame_time > self.frame_delay:
                    self.last_frame_time = now
                    self.current_frame_index = (self.current_frame_index + 1) % 2

                if self.state == "move_left":
                    self.image = self.walk_frames_left[self.current_frame_index]
                else:
                    self.image = self.walk_frames_right[self.current_frame_index]
        def update(self, dt):
            self.update_state()

            velocity_x = 0
            if self.state == "move_left":
                velocity_x = -self.speed
            elif self.state == "move_right":
                velocity_x = self.speed

            self.rect.x += int(velocity_x * dt)

            self.update_animation()

        def draw(self, surface, offset_x):
            screen_x = self.rect.x - offset_x
            surface.blit(self.image, (screen_x, self.rect.y))
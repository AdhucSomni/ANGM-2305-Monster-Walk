import pygame
import sys

def main():
    """
    Main game loop function.

    Initializes pygame, sets up the display, loads class objects, scales background, 
    runs the main game loop to handle events, and updates.
    """
    pygame.init()

    info = pygame.display.Info()
    screen_w, screen_h = info.current_w, info.current_h

    screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Monster-Walk")

    clock = pygame.time.Clock()
    fps = 60

    background = pygame.image.load("background/sunny_day.png").convert()

    w, h = background.get_size()
    scale = screen_h / h
    background_w = int(w * scale)
    background = pygame.transform.scale(background, (background_w, screen_h))

    ground_y = screen_h - 80
    player = Player((screen_w //w, ground_y))
    camera = Camera(screen_w)

    running = True
    while running:
        dt = clock.tick(fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move_left = True
                elif event.key == pygame.K_d:
                    player.move_right = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.move_left = False
                elif event.key == pygame.K_d:
                    player.move_right = False

        player.update(dt)
        camera.follow(player.rect)

        offset_x = camera.offset_x

        start_x = -offset_x % background_w
        x = start_x - background_w
        while x < screen_w:
            screen.blit(background, (x, 0))
            x += background_w
        
        player.draw(screen, offset_x)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

class Camera:
    """
    Camera class for following the player along the x-axis.
    Keeps sprite cenetered on the screen as it moves.
    """
    def __init__(self, screen_w):
        """
        Initializes the camera class.
        
        :param screen_w: Width of the game window in pixels.
        """
        self.offset_x = 0
        self.screen_w = screen_w

    def follow(self, rect):
        """
        updates camera position to follow a target rectangle.

        Centers the camera on the target's horizontal center position to keep target
        appearing in the middle of the window.
        
        :param rect: the target rectangle to follow. (centered on player)
        :type rect: pygame.Rect
        """
        self.offset_x = rect.centerx - self.screen_w // 2

class Player(pygame.sprite.Sprite):
    """ 
    Player sprite class with movement and animation.
    
    Handles player movement, animation states (idle and moving),
    and drawing with direction specific sprite pngs.
    """

    def __init__(self, start_pos):
        """
        Initializes the player class.
        
        :param start_pos: the starting (x, y) position for the sprites midbottom.
        :type start_pos: tuple 
        """
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
        """
        Docstring for load_frames
        
        :param self: Description
        """
        def load(name):
            """
            Docstring for load
            
            :param name: Description
            """
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
        """
        Docstring for update_state
        
        :param self: Description
        """
        if self.move_left and not self.move_right:
            self.state = "move_left"
            self.facing_left = True
        elif self.move_right and not self.move_left:
            self.state = "move_right"
            self.facing_left = False
        else:
            self.state = "idle"

    def update_animation(self):
        """
        Docstring for update_animation
        
        :param self: Description
        """
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
        """
        Docstring for update
        
        :param self: Description
        :param dt: Description
        """
        self.update_state()

        velocity_x = 0
        if self.state == "move_left":
            velocity_x = -self.speed
        elif self.state == "move_right":
            velocity_x = self.speed

        self.rect.x += int(velocity_x * dt)

        self.update_animation()

    def draw(self, surface, offset_x):
        """
        Docstring for draw
        
        :param self: Description
        :param surface: Description
        :param offset_x: Description
        """
        screen_x = self.rect.x - offset_x

        bob = 0
        if self.state != "idle":
                if self.current_frame_index == 0:
                    bob = 2
                else:
                    bob = -2

        surface.blit(self.image, (screen_x, self.rect.y + bob))

if __name__ == "__main__":
    main()
import pygame
import sys
import os

from player import Player
from camera import Camera

def main():
    pygame.init()

    display_info = pygame.display.Info()
    screen_width, screen_height = display_info.current_w, display_info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Monster-Walk")

    clock = pygame.time.Clock()
    fps = 60

    background = pygame.image.load("background/sunny_day.png")
    bg_original_width, bg_original_height = background.get_size()

    scale_fac = screen_height / bg_original_height
    bg_width = int(bg_original_width * scale_fac)
    bg_height = screen_height
    background = pygame.transform.scale(background, (bg_width, bg_height))

    BG_WIDTH, BG_HEIGHT = background.get_size()

    #temp background while background png is finalized
    #sky_color = (135, 206, 235) #light blue
    #ground_color = (90, 180, 90) #green

    #ground_height = 120
    ground_y = screen_height - 40
    player = Player(start_pos=(screen_width // 2, ground_y))

    camera = Camera(screen_width)

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

        player.update(dt, screen_width)
        camera.follow(player.rect)

        offset_x = camera.offset_x

        start_x = -offset_x % BG_WIDTH
        y= 0
        
        
        player.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
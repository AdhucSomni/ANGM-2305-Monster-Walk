import pygame
import sys
from player import Player

def main():
    pygame.init()

    display_info = pygame.display.Info()
    SCREEN_WIDTH, SCREEN_HEIGHT = display_info.current_w, display_info.current_h

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Monster-Walk")

    clock = pygame.time.Clock()
    fps = 60

    #temp background while background png is finalized
    sky_color = (135, 206, 235) #light blue
    ground_color = (90, 180, 90) #green

    ground_height = 120
    ground_y = SCREEN_HEIGHT - 40

    player = Player(start_pos=(SCREEN_WIDTH // 2, ground_y))

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

        player.update(dt, SCREEN_WIDTH)

        screen.fill(sky_color)

        ground = pygame.Rect(
            0,
            SCREEN_HEIGHT - ground_height,
            SCREEN_WIDTH,
            ground_height
        )
        pygame.draw.rect(screen, ground_color, ground)

        player.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
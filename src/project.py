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
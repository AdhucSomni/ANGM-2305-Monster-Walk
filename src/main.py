import pygame
import sys
from player import Player

def main():
    pygame.init()

    display = pygame.display.Info()
    screen_width, screen_height = display.current_w, display.current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    
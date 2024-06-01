from pygame.locals import *
import pygame
import src.params


class Images:
    def __init__(self):
        image_path = src.params.image_path
        self.player_img = pygame.image.load(image_path + src.params.player_img).convert()
        self.block_img = pygame.image.load(image_path + src.params.wall_img).convert()
        self.goal_img = pygame.image.load(image_path + src.params.goal_img).convert()
        self.win_img = pygame.image.load(image_path + src.params.win_img).convert()

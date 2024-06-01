"""
Using abstract factory pattern for MazeApp Class
Maze object instantiation is deferred to factory
AbstractFactory class only defines abstract methods 'build_qa_maze' and 'build_exp_maze' and hte arguments
the implementation of 'build_qa_maze' and 'build_exp_maze' is deferred to Factory class so in the future, if other
approaches of maze creation are desired, another factory can be easily created and inherits from AbstractFactory
making it easier to expand and maintain
"""
import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod
import src.params
from src.maze.Maze import *
from src.maze.MazeTest import *


class AbstractFactory:
    # build maze for QA / inspection / test purpose
    @staticmethod
    @abstractmethod
    def build_qa_maze(block_size, dim, maze_id):
        pass

    # build maze for real experiment
    @staticmethod
    @abstractmethod
    def build_exp_maze(block_size, dim, maze_id):
        pass


class Factory(AbstractFactory):
    # build maze for QA / inspection / test purpose
    @staticmethod
    def build_qa_maze(block_size, dim, maze_id):
        return MazeTest(block_size, dim, maze_id)

    # build maze for real experiment
    @staticmethod
    def build_exp_maze(block_size, dim, maze_id):
        return Maze(block_size, dim, maze_id)

    # check if a quit request has been submitted during the loop
    @staticmethod
    def check_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    # final clean up by quitting the game
    @staticmethod
    def maze_cleanup():
        pygame.quit()

    # set pygame display
    @staticmethod
    def set_display(window_width, window_height):
        return pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE)

    # set pygame menu caption
    @staticmethod
    def set_caption(caption):
        pygame.display.set_caption(caption)

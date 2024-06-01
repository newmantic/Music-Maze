"""
The Maze class is to define, to load and to draw a maze from a file. Note that new maze can be generated and saved to 
files by MazeGenerator class. It inherits MazeABC for basic maze functions and has a sophisticated maze loading function
 that can generate new mazes in case that the maze files with defined maze ids cannot be found or the experimenter finds
 the mazes too easy / too difficult and would like to generate a new one.
 The hierarchical structure: ABC -> MazeABC -> Maze / MazeTest
"""

import os
import math
import time
import pygame_menu
from pygame import mixer
from pygame.locals import *
from pygame_menu import themes
from src.maze.MazeGenerator import *
from src.maze.MazeABC import *


class Maze(MazeABC):
    def __init__(self, block_size, dim, maze_id):
        # instantiate with the parent class
        super().__init__(block_size, dim, maze_id)

    # load maze from file
    def load_maze(self, maze_file):
        # if a maze file with the specific maze_id does not exist, generate a new maze and save it
        if not os.path.isfile(self.maze_path + maze_file):
            print('generate maze: ' + self.maze_path + maze_file)
            maze_generator = MazeGenerator(nx=self.dimension_convert(self.M), ny=self.dimension_convert(self.N))
            maze_generator.generate_maze(self.maze_id)
        #  once we assure that a maze with the desired maze_id exists or has been generated, we can load the maze
        with open(self.maze_path + maze_file) as file:
            print('load maze: ' + self.maze_path + maze_file)
            maze = []
            for line in file:
                # convert lines in the maze file to a list
                maze.extend(line.rstrip().lstrip().split(',')[:-1])
        # convert string to integer (0, 1)
        number_maze = [int(item) for item in maze]
        return number_maze


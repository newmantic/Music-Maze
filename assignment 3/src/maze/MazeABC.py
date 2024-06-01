"""
The Maze class is to define, to load and to draw a maze from a file. Note that new maze can be generated and saved to 
files by MazeGenerator class. The hierarchical structure: ABC -> MazeABC -> Maze / MazeTest
"""

import pygame
import src.params
from abc import ABC, abstractmethod


class MazeABC(ABC):
    def __init__(self, block_size, dim, maze_id):
        self.maze_path = src.params.maze_path
        self.block_size = block_size
        self.M = dim
        self.N = dim
        self.maze_id = maze_id
        self.maze_file = src.params.maze_name + '_' + str(maze_id) + '.txt'
        self.maze = self.load_maze(self.maze_file)
        self.maze_convert(dim)
        self.entry = [0, 1]
        self.sortie = [int(src.params.dim - 1), 1]

    # load maze from file / can be overridden as a simply copy-pasted pre-made maze for testing
    @abstractmethod
    def load_maze(self, maze_file):
        pass

    # convert block dimension to wall-pair dimension for new maze generation
    @staticmethod
    def dimension_convert(length):
        return int((length-1)/2)

    # loaded maze is a list, needs to be converted to several rows
    def maze_convert(self, dim):
        new_maze = []
        # convert row by row, with a fixed row length = dim
        for i in range(dim):
            row = []
            for j in range(dim):
                index = i*dim + j
                row.append(self.maze[index])
            # add the converted row to new maze
            new_maze.append(row)
        # the new_maze will be accessed by player class
        self.new_maze = new_maze
        # print(new_maze)

    # draw maze on pygam display surface
    def draw(self, display_surf, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            # check if it is a wall
            if self.maze[bx + (by * self.M)] == 1:
                # draw a wall
                display_surf.blit(image_surf, (bx * self.block_size, by * self.block_size))
            # scanning from left to right
            bx = bx + 1
            # then scanning from top row to bottom row
            if bx > self.M - 1:
                bx = 0
                by = by + 1

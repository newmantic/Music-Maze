"""
MazeGenerator makes new mazes if the experiment needs more mazes for random test then it saves generated mazes into
files to be loaded by Maze class. A maze is composed by a grid of blocks. A block is composed of a 2 x 2 grid
 itself - so an M x N maze will have M x N blocks but (2M + 1) x (2N + 1) wall (denoted by 1) or space (denoted by 0)
 cells.

To generate a maze, remember that  a maze cannot have the formation: 1, 1  or  0, 0  or  1, 0  or  0, 1
                                                                     1, 1      0, 0      0, 1      1, 0

As a result, a block should be chosen from one of the following options:
 (a) 0, 0       (b) 0, 1        (c) 0, 0        (d) 0, 1
     1, 1           1, 1            0, 1            0, 1
An (1, 0) or (1, 1) in the upper row of a block is not feasible because we already have an outer wall and a maze cannot
have the formation: 1, 1  or  1, 0
                    1, 1      0, 1
Similarly, an (1, 0) or (0, 0) in the lower row of a block is not feasible because a maze cannot have the formation:
                    0, 0  or  0, 1
                    0, 0      1, 0

So blocks can be distinguished by 'wall' conditions:
(a) & (b) has a south wall; (c) and (d) do not
(b) & (d) has an east wall; (a) and (c) do not
This is how we can generate a maze thorough block selection via wall condition
"""

import random
import src.params
from src.maze.Block import *


class MazeGenerator:
    # a maze is composed by a grid of blocks
    def __init__(self, nx, ny, ix=0, iy=0):
        # Maze pair size (maze dimension = Maze pair size x 2 + 1)
        # where nx, ny are maze dimensions, and ix, iy are maze entry position so will be allocated a 0
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Block(x, y) for y in range(ny)] for x in range(nx)]

    # return the block object
    def block_at(self, x, y):
        return self.maze_map[x][y]

    # to print out the maze in 0/1: o is the space, 1 is the wall
    def __str__(self):
        # first wall have an entrance at the position 1, all others are walls
        maze_rows = ['1, 0, ' + '1, ' * (self.nx-1) * 2 + '1, ']
        # iterate through each row of a maze: four options: (0, 1), (0, 0), (1, 1), (1, 0)
        for y in range(self.ny):
            # start with the outer wall
            maze_row = ['1, ']
            # if a block has an east wall, then it is a space with a wall to the east, so it will have space-wall,
            # which can be denoted as (0, 1). If not, then it is space-space, which is (0, 0)
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append('0, 1, ')
                else:
                    maze_row.append('0, 0, ')
            maze_rows.append(''.join(maze_row))
            # again start with the outer wall
            maze_row = ['1, ']
            # if a block has a south wall,then (1, 1) is allocated, otherwise (0, 1) is allocated
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('1, 1, ')
                else:
                    maze_row.append('0, 1, ')
            # make an exit of the maze
            if y == self.ny - 1:
                maze_row[1] = '0, 1, '
            maze_rows.append(''.join(maze_row))
        # return the maze composed of blocks
        return '\n'.join(maze_rows)

    # to check neighbours of a block to see whether it has all four walls - fatal for a maze. Consequently,
    # and some walls must later be removed. For now we simply put those with four walls on a black list
    def find_blacklisted_neighbours(self, block):
        # four neighbours of a block positioned by a list of directional difference (delta)
        # west (position: x-1, y), east (position: x+1, y), south (position: x, y+1), north (position: x, y-1)
        delta = [('W', (-1, 0)), ('E', (1, 0)), ('S', (0, 1)), ('N', (0, -1))]
        neighbours = []
        # iterate through a list of directional difference
        for direction, (dx, dy) in delta:
            # locate a neighbour
            x2, y2 = block.x + dx, block.y + dy
            # boundary condition check
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                # identify a neighbour
                neighbour = self.block_at(x2, y2)
                # check whether the neighbour has all four walls; if it does, put it on the blacklist
                if neighbour.check_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    # to create a new maze
    def make_maze(self):
        # define the number of blocks to be formed and validated
        n = self.nx * self.ny
        # this is the passage where a player can move in a maze
        maze_passage = []
        # define the current block to investigate
        current_block = self.block_at(self.ix, self.iy)
        # this is the total number of visited blocks during maze construction
        nv = 1

        # while not all blocks are validated ...
        while nv < n:
            # find neighbours with all four walls
            neighbours = self.find_blacklisted_neighbours(current_block)
            if not neighbours:
                # if no neighbours, we are at a dead-end and need to backtrack from the current maze passage
                current_block = maze_passage.pop()
                continue
            # choose a random neighbouring block and iterate to it
            direction, next_block = random.choice(neighbours)
            # since the neighbour has all four walls, at least one must be removed. The wall between the current block
            # and the blacklisted neighbour with four walls is removed
            current_block.remove_wall(next_block, direction)
            # we add the current block into the maze passage
            maze_passage.append(current_block)
            # then the player moves from current block to the next block
            current_block = next_block
            nv += 1

    # this is to save a generated new make to a file
    def generate_maze(self, maze_id):
        maze_file = src.params.maze_name + '_' + str(maze_id) + '.txt'
        # make a maze
        self.make_maze()
        # print(maze)
        # save the maze to file
        with open(src.params.maze_path + maze_file, 'w') as f:
            for line in self.__str__():
                f.write(line)

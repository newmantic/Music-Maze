"""
 Block is a building component of a maze, and a maze is composed by a grid of blocks. A block is composed of a 2x2 grid
 itself - so an M x N maze will have M x N blocks but (2M + 1) x (2N + 1) wall/space cells. A block has the following
 formation options:
 (a) 0, 0       (b) 0, 1        (c) 0, 0        (d) 0, 1
     1, 1           1, 1            0, 1            0, 1
An (1, 0) or (1, 1) in the upper row of a block is not feasible because we already have an outer wall and a maze cannot
have the formation: 1, 1
                    1, 1
Similarly, an (1, 0) or (0, 0) in the lower row of a block is not feasible because a maze cannot have the formation:
                    0, 0
                    0, 0
Blocks are initialised to have all walls, and by the function remove_wall, it can be made into (a), (b), (c) or (d)
"""


class Block:
    # A wall is defined to separate a pair of blocks
    def __init__(self, x, y):
        # define a block position by x, y
        self.x, self.y = x, y
        # initially, we make all blocks surrounded by walls
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
        # in a 2D maze setting, wall pairs are opposite directional pairs
        self.wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    # to check whether a block is surrounded by all walls
    def check_all_walls(self):
        # check whether a block has all its walls
        return all(self.walls.values())

    def remove_wall(self, other, wall):
        # if there is a wall between a block (self) and another block (other)
        # the function removes the specified wall
        self.walls[wall] = False
        other.walls[self.wall_pairs[wall]] = False


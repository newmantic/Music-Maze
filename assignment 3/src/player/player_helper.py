"""
PlayerHelper class is to define auxiliary methods for player class
PlayerHelper is a Mixins class, using wrappers and lambda to facilitate direction checking
"""

from re import search
from functools import wraps
import math
import time


# define a wrapper to be used on class method for condition checking, I also use wraps from functools and search from re
# (regular expression) by matching lambda function (of self) with condition_name. It's main purpose is to check
# directions moving on x-axis and moving on y-axis will result in different behaviours in a maze, and this check needs
# to be frequently carried out. A wrapper will thus make codes cleaner here.
def check_condition(lambda_func, condition_name):
    def wrapper(passed_func):
        @wraps(passed_func)
        def wrapped(self, *args, **kwargs):
            # checking lambda is callable and that lambda expression matches with re condition_name
            # the patter will simply be 'x' or 'y'
            if callable(lambda_func) and search(condition_name, (lambda_func(self) or '')):
                # only execute the function when the condition_name matches with lambda expression
                passed_func(self, *args, **kwargs)
        return wrapped
    return wrapper


class PlayerHelper:
    # only change x position if move on x-axis
    @check_condition(lambda m: m.axis, 'x')
    def move_x(self, steps):
        self.x = self.x + self.block_size * steps

    # only change y position if move on y-axis
    @check_condition(lambda m: m.axis, 'y')
    def move_y(self, steps):
        self.y = self.y + self.block_size * steps

    # only assign i to fixed position to y if move on x-axis
    @check_condition(lambda m: m.axis, 'x')
    def pos_x(self):
        self.current_y = self.convert_pixel_to_matrix(self.y, self.block_size)

    # only assign fixed position to x if move on y-axis
    @check_condition(lambda m: m.axis, 'y')
    def pos_y(self):
        self.current_x = self.convert_pixel_to_matrix(self.x, self.block_size)

    # only assign i to current_x if move on x-axis
    @check_condition(lambda m: m.axis, 'x')
    def direction_x(self, i):
        self.current_x = i

    # only assign i to current_y if move on y-axis
    @check_condition(lambda m: m.axis, 'y')
    def direction_y(self, i):
        self.current_y = i

    # convert continuous pixels into discrete positions
    @staticmethod
    def convert_pixel_to_matrix(pixel, block_size):
        ind = round(pixel/block_size)
        return ind

    # calculate steps of move given origin and destination pixels
    @staticmethod
    def convert_move_to_matrix(org_pixel, des_pixel, block_size):
        # ceiling operation should be applied is destination > origin
        if des_pixel >= org_pixel:
            ind = math.ceil(des_pixel/block_size)
        # flooring operation should be applied is destination < origin
        else:
            ind = math.floor(des_pixel//block_size)
        return ind

    # change position to the direction steps
    def move_change(self, steps):
        self.move_x(steps)
        self.move_y(steps)

    # confirm current position x or y depending on movement direction
    def current_direction(self):
        # self.current_x, self.current_y = -1, -1
        self.pos_x()
        self.pos_y()

    # based on movement direction, and the corresponding axis, update current position
    def moving_direction(self, i):
        self.direction_x(i)
        self.direction_y(i)

    # check the position is an empty space, not a wall
    def pos_check(self, new_x, new_y):
        if self.maze.new_maze[new_y][new_x] == 0:
            return True
        return False

    # move the player in the maze in a discrete and non-continuous way and stop before the wall
    def one_step(self, pos, axis):
        # define origin and destination's discrete positions, and then final position, such that the player won't go
        # through the wall; as destination is related to key speed, sometimes it's too large, and without proper check,
        # the player will go through the wall. We thus need to: 1) make movement discrete; 2) calculate the logically
        # feasible final position given the origin and the destination from the keyboard
        # first dealing with x-axis (horizontal) movement
        if axis == 'x':
            org = self.convert_pixel_to_matrix(self.x, self.block_size)
            des = self.convert_move_to_matrix(self.x, pos, self.block_size)
        # then dealing with y-axis (vertical) movement
        else:
            org = self.convert_pixel_to_matrix(self.y, self.block_size)
            des = self.convert_move_to_matrix(self.y, pos, self.block_size)
        # define the sign of movement by comparing discrete origin and destination positions
        steps = 1 if des >= org else -1
        # we then need to scan all points between origin and destination, and stop the player if it hits a wall
        self.multiple_move(axis, org, des, steps)

    # iterate from original position (org) to destinations (des)
    def multiple_move(self, axis, org, des, steps):
        # if horizontal move, find the y position first, else if vertical move, find the x position first
        self.current_direction()
        # check all points in the horizontal direction between the origin and destination
        for i in range(org + steps, des + steps, steps):
            # stop the player movement if it hits a wall on a horizontal path or on a vertical path
            self.moving_direction(i)
            if self.pos_check(self.current_x, self.current_y):
                self.move_change(steps)
                if self.check_exit(self.x, self.y):
                    break
            else:
                break

    # keep track of time elapsed for recording the results
    def measure_time(self):
        self.time_elapsed.append([time.time() - self.start_time, self.convert_pixel_to_matrix(self.x, self.block_size),
                                  self.convert_pixel_to_matrix(self.y, self.block_size)])


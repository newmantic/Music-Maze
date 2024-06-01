"""
Player is the class that defines the player icon movement in the maze
the objectives are: 1) move discretely and not continuously; 2) cannot go through any wall in a maze
"""

from src.experiment_control.ExperimentResult import *
from src.player.player_helper import *


class Player(PlayerHelper):
    def __init__(self, block_size, dim, maze, individual_id, maze_id, music_tempo, demographics_data):
        self.block_size = block_size
        self.dim = dim
        self.maze = maze
        self.individual_id = individual_id
        self.maze_id = maze_id
        self.music_tempo = music_tempo
        self.demographics_data = demographics_data
        self.x = block_size*self.maze.entry[1]
        self.y = block_size**self.maze.entry[0]
        self.exit_x = block_size*self.maze.sortie[1]
        self.exit_y = block_size*self.maze.sortie[0]
        self.results = ExperimentResult()
        self.speed = block_size*0.1
        self.sleep = 0.1
        self.freeze = 0
        self.current_x = -1
        self.current_y = -1
        self.start_time = None
        self.axis = None
        self.time_elapsed = []

    # define movement given axis and direction
    def key_movement_direction(self, axis, direction):
        self.axis = axis
        self.measure_time()
        time.sleep(self.sleep)
        base_pos = self.x if axis == 'x' else self.y
        pos = base_pos + direction*self.speed
        # cannot move out of the maze, the minimum x, y position is 0
        pos = max(pos, 0)
        if self.freeze == 0:
            self.one_step(pos, axis)

    # right key movement, add a tiny sleep for visibility; only allow to move if not frozen/reached the destination
    def move_right(self):
        self.key_movement_direction(axis='x', direction=1)

    # left key movement, add a tiny sleep for visibility; only allow to move if not frozen/reached the destination
    def move_left(self):
        self.key_movement_direction(axis='x', direction=-1)

    # up key movement, add a tiny sleep for visibility; only allow to move if not frozen/reached the destination
    def move_up(self):
        self.key_movement_direction(axis='y', direction=-1)

    # down key movement, add a tiny sleep for visibility; only allow to move if not frozen/reached the destination
    def move_down(self):
        self.key_movement_direction(axis='y', direction=1)

    # check whether the player reaches the exit of the maze
    def check_exit(self, x, y):
        # if the player's position is at the exit (sortie in French)
        if round(x/self.block_size) == self.maze.sortie[1] and round(y/self.block_size) == self.maze.sortie[0]:
            # freeze it
            self.freeze = 1
            # record time
            self.measure_time()
            # save individual, move by move result with correspondent time elapsed of each key stroke
            self.results.save_individual_result(self.individual_id, self.maze_id, self.time_elapsed, self.music_tempo)
            # save aggregated result in standard format, where each row represent a maze test; only the total time
            # elapsed is recorded; participant's ID, demographic information, as well as maze ID, music speed ID,
            # are also recorded
            self.results.save_aggregated_results(self.individual_id, self.maze_id, self.time_elapsed, self.music_tempo,
                                                 self.demographics_data)
            # save the maze/music configuration into memory
            self.results.append_file(self.results.record_file, (self.maze_id, self.music_tempo))
            # save participant ids into memory
            self.results.append_file(self.results.participant_file, self.individual_id)
            # clean up results after saving
            self.results.reset()
            # return True for the exit
            return True
        else:
            return False

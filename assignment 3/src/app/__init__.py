"""
This is the main experiment control that interacts with menus, maze, player, music and experiment memories and settings
"""

import math
import time
import pygame
from pygame.locals import *
import src.params
from src.maze.Maze import *
from src.maze.MazeTest import *
from src.player import *
from src.menus import *
from src.media.Music import *
from src.media.Images import *
from src.experiment_control.ExperimentMemory import *
from src.app.app_factory import *


class MazeApp:
    def __init__(self, block_size, dim, **kwargs):
        self.block_size = block_size
        self.dim = dim
        self.dev_test = kwargs['dev_test']
        self.music_on = kwargs['music_on']
        self._running = False
        self.display_img = None
        self.demographics_data = None
        self.menus = None
        self.maze = None
        self.player = None
        self.music = None
        self.images = None
        self.maze_id = None
        self.tempo = None
        self.individual_id = None
        self.test_count = 0
        self.num_tests = src.params.num_tests
        self.windowWidth = self.block_size * self.dim
        self.windowHeight = self.block_size * self.dim
        self.memory = ExperimentMemory()
        self.factory = Factory()

    # initialise a maze game by set the screen and create menus
    def maze_init(self):
        pygame.init()
        self.maze_screen_renew()
        self.menus = Menus(self.windowWidth, self.windowHeight, self.start_the_game, self.continue_the_game,
                           self.maze_reset)
        self.menus.make_menus()
        self.menu_loop()

    # to start a new session of maze, by a new participant; a new id is assigned
    def start_the_game(self):
        if self.menus.check_demographics(src.params.legal_age):
            self.individual_id = self.memory.id_assignment()
            self.prepare_new_maze()

    # to start a new session of maze, by an existing participant; do not assign a new id
    def continue_the_game(self):
        if self.menus.check_demographics(src.params.legal_age):
            # self.individual_id = self.memory.id_assignment()
            self.prepare_new_maze()

    # end the game: reset everything and go to end menu
    def end_the_game(self):
        self.show_congratulations()
        self.stop_maze()
        self.test_count = 0
        self.maze_screen_renew()
        self.menus.go_to_menu(self.menus.end)
        self.menu_loop()

    # end the session: to show congratulation message, stop maze, renew screem and go to acknowledgement menu
    def end_the_session(self):
        self.show_congratulations()
        self.stop_maze()
        self.maze_screen_renew()
        self.menus.go_to_menu(self.menus.acknowledge)
        self.menu_loop()

    # keep displaying menu by running a loop
    def menu_loop(self):
        while not self._running:
            events = pygame.event.get()
            self.factory.check_quit(events)
            self.menus.main_menu_looping(events, self.display_img)
            pygame.display.update()

    # get a new maze ready, create a player, load demographic data from menu, start music and start to count time
    def prepare_new_maze(self):
        self.maze_id, self.tempo = self.memory.randomise_condition(self.individual_id)
        self._running = True
        self.images = Images()
        self.demographics_data = self.menus.return_demographics()
        # print(self.demographics_data)
        self.get_maze()
        self.player = Player(self.block_size, self.dim, self.maze, self.individual_id, self.maze_id, self.tempo,
                             self.demographics_data)
        self.player.freeze = 0
        self.player.start_time = time.time()
        self.music = Music(self.tempo)
        self.player.start_time = time.time()

    # display congratulation message after the participant finished a maze
    def show_congratulations(self):
        self.display_img.blit(self.images.win_img, (0, 0))
        pygame.display.flip()
        time.sleep(1)

    # render maze images including player positions
    def maze_render(self):
        self.display_img.fill((0, 0, 0))
        self.display_img.blit(self.images.goal_img, (self.player.exit_x, self.player.exit_y))
        self.display_img.blit(self.images.player_img, (self.player.x, self.player.y))
        self.maze.draw(self.display_img, self.images.block_img)
        if self.player.freeze == 1:
            self.test_count += 1
            # if the number of tests completed is smaller than desired number of tests, continue the test
            # by presenting a new maze/music setup while keeping the current demographic information
            if self.test_count < self.num_tests:
                self.end_the_session()
            # else if the participant has completed the desired number of tests, end the game,
            # reset demographic information, and back to the main menu
            else:
                self.end_the_game()
        pygame.display.flip()

    # main function to be called to execute the maze game, including direction movement control using keyboard
    def maze_execute(self):
        self.maze_init()
        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                self.player.move_right()
            if keys[K_LEFT]:
                self.player.move_left()
            if keys[K_UP]:
                self.player.move_up()
            if keys[K_DOWN]:
                self.player.move_down()
            if keys[K_ESCAPE]:
                self._running = False
            self.maze_render()
        self.factory.maze_cleanup()

    # to stop maze game after a session, erase current player and maze, stop music
    def stop_maze(self):
        self._running = False
        self.music.stop_music()
        self.maze = None
        self.player = None

    # to end all maze games after the participant finished the desired number of tests,
    # erase current player and maze, stop music, clean demographic information and reset test_count
    def maze_reset(self):
        self.stop_maze()
        self.display_img = None
        self.demographics_data = None
        self.menus = None
        self.test_count = 0
        self.maze_init()

    def get_maze(self):
        if self.dev_test:
            self.maze = self.factory.build_qa_maze(self.block_size, self.dim, self.maze_id)
        else:
            self.maze = self.factory.build_exp_maze(self.block_size, self.dim, self.maze_id)

    # renew the maze screen
    def maze_screen_renew(self):
        self.display_img = self.factory.set_display(self.windowWidth, self.windowHeight)
        self.factory.set_caption(src.params.menu_caption)

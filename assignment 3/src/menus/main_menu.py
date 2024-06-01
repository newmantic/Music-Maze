"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of main menu
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinMainMenu(CustomMenu):
    def make_main_menu(self):
        # Creating the main menu
        player_img = pm.baseimage.BaseImage(src.params.image_path + src.params.player_img)
        goal_img = pm.baseimage.BaseImage(src.params.image_path + src.params.goal_img)
        ucl_img = pm.baseimage.BaseImage(src.params.image_path + src.params.UCL_img)
        self.main_menu = self.menu_default_theme(src.params.main_menu_caption)
        self.main_menu.menu_default_layout(32)
        # Adjusting the default values
        self.main_menu.widget_alignment = pm.locals.ALIGN_CENTER
        self.main_menu.add.label(title=src.params.welcome, font_color=src.params.BLACK, font_size=36)
        self.main_menu.add.label(title=src.params.instruction_1, font_color=src.params.BLACK, font_size=20)
        self.main_menu.add.label(title="    ", background_color=player_img)
        self.main_menu.add.label(title=src.params.instruction_2, font_color=src.params.BLACK, font_size=20)
        self.main_menu.add.label(title=src.params.instruction_3, font_color=src.params.BLACK, font_size=20)
        self.main_menu.add.label(title="     ", background_color=goal_img)
        self.main_menu.add_button(title="", font_size=1, align=pm.locals.ALIGN_LEFT)
        self.main_menu.add.label(title=src.params.instruction_4, font_color=src.params.BLACK, font_size=20)

        # add start button that takes to the demographics menu when clicked
        self.main_menu.add.label(title="")
        self.main_menu.add_button(title=" Join ", action=self.to_consent_menu)
        # An empty label that is used to add a separation between the two buttons
        self.main_menu.add.label(title="")
        self.main_menu.add_button(title=" Quit ", action=pm.events.EXIT)
        # display the UCL logo
        self.main_menu.add.label(title="")
        self.main_menu.add.label(title="                                                                         ",
                                 font_size=40, background_color=ucl_img)


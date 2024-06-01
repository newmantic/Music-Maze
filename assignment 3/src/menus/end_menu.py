"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of end menu
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinEndMenu(CustomMenu):
    # for participants who have finished the desired amount of mazes, final screen to go back to the main menu
    def make_end_menu(self):
        self.end = self.menu_default_theme("Thank you for your participation.")
        # Adjusting the default values
        self.end.menu_default_layout(14)
        self.end.add.label(title=src.params.end_text, align=pm.locals.ALIGN_CENTER)
        # make space
        self.end.add.label(title="")
        self.end.add_button(title="", font_size=1, align=pm.locals.ALIGN_LEFT)
        # add button to go back to the main menu - the only option as the participant has completed the desired number
        # of mazes
        self.end.add_button(title="Exit", action=self.reset_game_func)

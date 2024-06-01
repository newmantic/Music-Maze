"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of acknowledgement menu
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinAckowledgeMenu(CustomMenu):
    # acknowledge the completion of a maze, offer options to continue or to quit
    def make_acknowledge_menu(self):
        self.acknowledge = self.menu_default_theme("You successfully completed a maze.")
        # Adjusting the default values
        self.acknowledge.menu_default_layout(14)
        self.acknowledge.add.label(title=src.params.acknowledge_text, align=pm.locals.ALIGN_CENTER)
        # make space
        self.acknowledge.add.label(title="")
        self.acknowledge.add_button(title="", font_size=1, align=pm.locals.ALIGN_LEFT)
        # add button to continue the next maze
        self.acknowledge.add_button(title="Next Experiment", action=self.continue_game_func)
        # make space
        self.acknowledge.add.label(title="")
        # add button to quit
        self.acknowledge.add_button(title="Quit Experiment ", action=self.reset_game_func)

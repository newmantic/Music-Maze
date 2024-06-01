"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of different menu utilities
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinMenuUtils(CustomMenu):
    # create all needed menus, in reverse order except for the main menu, so the former objects created can be
    # called by latter objects
    def make_menus(self):
        self.make_main_menu()
        self.make_end_menu()
        self.make_acknowledge_menu()
        self.make_demographics_menu()
        self.make_consent_menu()

    # go to the desired menu
    def go_to_menu(self, menu):
        self.main_menu.go_to_menu(menu)

    # print out demographics information for inspection
    def print_demographics(self):
        print("\n\n")
        # getting the data using "get_input_data" method of the Menu class
        demographics_data = self.demographics.get_input_data()
        for key in demographics_data.keys():
            print(f"{key}\t:\t{demographics_data[key]}")

    # show missing or not compatible user input
    def show_error(self, error_info):
        self.feedback_widget.update_font({'color': src.params.RED})
        self.feedback_widget.set_title(error_info)

    # main menu update and draw loop
    def main_menu_looping(self, events, figure):
        if self.main_menu.is_enabled():
            self.main_menu.update(events)
            self.main_menu.draw(figure)

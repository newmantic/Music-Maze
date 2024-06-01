"""
Menus for the experiment inputs and flow control
The Class Menus uses a multiple inheritance with mixins, which have no data but methods, so we never call super().
The Class Menus has many methods, and they are arranged into different pygame_menu classes.
The hierarchical structure is: pygame_menu.Menu -> CustomMenu -> Mixins (multiple classes) -> Menus
"""
import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *
from src.menus.main_menu import *
from src.menus.demographics_menu import *
from src.menus.consent_menu import *
from src.menus.acknowledge_menu import *
from src.menus.end_menu import *
from src.menus.menu_utils import *


class Menus(MixinMainMenu, MixinDemographicsMenu, MixinConsentMenu, MixinAckowledgeMenu, MixinEndMenu, MixinMenuUtils):
    def __init__(self, window_width, window_height, start_game_func, continue_game_func, reset_game_func):
        self.window_width = window_width
        self.window_height = window_height
        self._ucl_img = pm.baseimage.BaseImage(src.params.image_path + src.params.UCL_img)
        self.start_game_func = start_game_func
        self.continue_game_func = continue_game_func
        self.reset_game_func = reset_game_func
        self.consent = None
        self.music_file = None
        self.demographics = None
        self.main_menu = None
        self.acknowledge = None
        self.end = None
        self.feedback_widget = None
        self.demographics_list = src.params.demographics_list

    def menu_default_theme(self, title):
        menu_obj = CustomMenu(title=title, width=self.window_width, height=self.window_height,
                              theme=pm.themes.THEME_DEFAULT)
        return menu_obj



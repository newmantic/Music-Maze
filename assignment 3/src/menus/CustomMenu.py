"""
The CustomMenu class is created to standardise the user input interface and information presentation.
I use Python’s built-in property decorator and property.setter to access the private _theme in pygame_menu.Menu class
which ie cleaner and easier to maintain. CustomMenu Class is to be inherited by ALL subsequent menu classes.
"""

import pygame_menu as pm
import src.params


class CustomMenu(pm.Menu, object):
    def __init__(self, title, width, height, theme):
        # standard menu theme, so code repetition is minimised and maintenance is easier
        super().__init__(title=title, width=width, height=height, theme=theme)
        self.default_colour = src.params.BLACK
        self.default_font = pm.font.FONT_PT_SERIF
        self.default_alignment = pm.locals.ALIGN_LEFT
        self.button_alignment = pm.locals.ALIGN_CENTER
        self._button_img = pm.baseimage.BaseImage(src.params.image_path + src.params.button_img)

    # define property widget_font_size
    @property
    def widget_font_size(self):
        return self._theme.widget_font_size

    # change the property widget_font_size
    @widget_font_size.setter
    def widget_font_size(self, font_size):
        self._theme.widget_font_size = font_size

    # define property widget_font_color
    @property
    def widget_font_color(self):
        return self._theme.widget_font_color

    # change widget_font_color
    @widget_font_color.setter
    def widget_font_color(self, color):
        self._theme.widget_font_color = color

    # define property widget_font
    @property
    def widget_font(self):
        return self._theme.widget_font

    # change widget_font
    @widget_font.setter
    def widget_font(self, font):
        self._theme.widget_font = font

    # define property widget_alignment
    @property
    def widget_alignment(self):
        return self._theme.widget_alignment

    # change widget_alignment
    @widget_alignment.setter
    def widget_alignment(self, alignment):
        self._theme.widget_alignment = alignment

    # set menu theme to all four default settings
    def menu_default_layout(self, font_size):
        self.widget_font_size = font_size
        self.widget_font_color = self.default_colour
        self.widget_font = self.default_font
        self.widget_alignment = self.default_alignment

    # open the specific menu for participants; basic block for menu flow control
    def go_to_menu(self, menu):
        self._open(menu)

    # add button with default button image, central alignment and default colour
    def add_button(self, align=None, font_color=None, background_color=None, **kwargs):
        if align is None:
            kwargs['align'] = self.button_alignment
        if background_color is None:
            kwargs['background_color'] = self._button_img
        if font_color is None:
            kwargs['font_color'] = self.default_colour
        self.add.button(**kwargs)


"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of content menu
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinConsentMenu(CustomMenu):
    def make_consent_menu(self):
        self.consent = self.menu_default_theme("Informed Consent Form")
        # Adjusting the default values
        self.consent.menu_default_layout(14)
        self.consent.add.label(title=src.params.consent_text)
        self.consent.add.label(title=src.params.agreement, align=pm.locals.ALIGN_CENTER)
        # separate space
        self.consent.add.label(title="")
        self.consent.add_button(title="", font_size=1, align=pm.locals.ALIGN_LEFT)
        self.consent.add_button(title="I AGREE", action=self.to_demographics_menu)

    # go to consent menu
    def to_consent_menu(self):
        self.main_menu.go_to_menu(self.consent)

"""
Menus for the experiment inputs and flow control
Mixin class for Menus, which have no data but methods. this is only to separate class functions into mixin classes
such that it is easier to maintain. Here are the methods of demographics menu
"""

import pygame_menu as pm
import src.params
from src.menus.CustomMenu import *


class MixinDemographicsMenu(CustomMenu):
    def make_demographics_menu(self):
        # Creating the demographics menu self.window_width, self.window_height
        self.demographics = self.menu_default_theme("UCL CoDes 23/24")
        # Adjusting the default values
        self.demographics.menu_default_layout(20)
        # add menu instruction text
        self.feedback_widget = self.demographics.add.label(title=src.params.user_input, font_color=src.params.BLACK,
                                                           font_size=20, label_id="info")
        # Text input that takes in participant's ID
        # self.demographics.add.text_input(title="Participant's ID : ", textinput_id="id")
        self.demographics.add.label(title="")
        self.demographics.add_button(title="", font_size=1, align=pm.locals.ALIGN_LEFT)
        self.demographics.add.label(title="Demographics ...", font_color=src.params.BLUE)
        # to adjust the age
        self.demographics.add.range_slider(title="Age ", default=1, range_values=(0, 120),
                                           increment=1, range_line_height=5, value_format=lambda x: str(int(x)),
                                           font_size=18, range_text_value_font_height=0.8,
                                           slider_text_value_font_height=1.2, rangeslider_id="age")
        # to select the gender
        self.demographics.add.dropselect(title="Gender", items=src.params.gender, font_size=18, dropselect_id="gender")
        # to select the ethnicity, multiple selections are allowed
        self.demographics.add.dropselect_multiple(title="Ethnicity", items=src.params.ethnicity, font_size=18,
                                                  dropselect_multiple_id="ethnicity", open_middle=True, max_selected=9,
                                                  selection_box_height=6)
        # to select the education level
        self.demographics.add.dropselect(title="Education Level", items=src.params.education, font_size=18,
                                         dropselect_id="education")
        # to select employment status
        self.demographics.add.selector(title="Employment\t", items=src.params.employment, font_size=18, default=0,
                                       selector_id="employment")

        # separate space
        self.demographics.add.label(title="Personality ...", font_color=src.params.BLUE)
        # personality test
        self.demographics.add.selector(title="I am more an ", items=src.params.attention, font_size=18, default=0,
                                       style="fancy", selector_id="attention")
        self.demographics.add.selector(title="I evaluate a situation by ", items=src.params.judgment, font_size=18,
                                       default=0, style="fancy", selector_id="judgment")
        self.demographics.add.selector(title="I make decisions by ", items=src.params.decision, font_size=18, default=0,
                                       style="fancy", selector_id="decision")
        self.demographics.add.selector(title="I approach changing environments by ", items=src.params.interaction,
                                       font_size=18, default=0, style="fancy", selector_id="interaction")

        # separate space
        self.demographics.add.label(title="Disability ...", font_color=src.params.BLUE)
        # Toggle switch to indicate specific disoriented condition
        self.demographics.add.toggle_switch(title="Topographical Disorientation", default=False, font_size=18,
                                            toggleswitch_id="topographical")
        # Toggle switch to indicate specific auditory condition
        self.demographics.add.toggle_switch(title="Auditory Disorder", default=False, font_size=18,
                                            toggleswitch_id="auditory")

        # separate space
        self.demographics.add.label(title="", font_size=8)
        self.demographics.add_button(title="  Resume Later  ", action=pm.events.BACK, font_size=18)
        # separate space
        self.demographics.add.label(title="", font_size=8)
        self.demographics.add_button(title="Start Experiment", action=self.start_game_func, font_size=18)

    # go to demographics menu
    def to_demographics_menu(self):
        self.main_menu.go_to_menu(self.demographics)

    # return demographic data
    def return_demographics(self):
        return self.demographics.get_input_data()

    # check demographic user input to be eligible for maze play
    def check_demographics(self, legal_age):
        demographics_data = self.demographics.get_input_data()
        # print(demographics_data)
        # check age
        if demographics_data['age'] < legal_age:
            self.show_error("Age " + f"{int(demographics_data['age'])} is too young!")
            return False
        # check missing field
        for demographic_info in self.demographics_list:
            if demographic_info not in demographics_data.keys():
                self.show_error("Missing " + f"{demographic_info}")
                return False
            elif (isinstance(demographics_data[demographic_info], tuple) and
                  (not isinstance(demographics_data[demographic_info][1], int)) and
                  (len(demographics_data[demographic_info][1]) == 0)):
                self.show_error("Missing " + f"{demographic_info}")
                return False
        self.feedback_widget.set_title(src.params.user_input)
        return True

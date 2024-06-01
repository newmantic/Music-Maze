"""
parameters used in the experiment
as the project is small I allow myself using params module; if the project is big, probably separating parameters in
yaml files will be a more adequate approach
"""

# _____ Critical Control Parameters ________________________________________#

# indicate whether it is for maze dev test or real maze experiment
# set False for real experiment; set True for experimenter QA
maze_dev = False

# indicate whether music should be on - music-off mode can be used to establish benchmarks
music_on = True

# no. of tests for each participant
num_tests = 2

# maze type list for maze files; ex: maze_1.txt, maze_2.txt, maze_3.txt, etc
# if no correspondent maze files are found, the system will automatically generate and save mazes to files for test
maze_ids = [1, 2]

# music speed list for music files; ex: myMusic_1.mp3, myMusic_2.mp3, myMusic_3.mp3, etc
music_speed = [1, 2, 3]

# maze dimension in blocks
dim = 17

# each block size in pixel
block_size = 44

# legal age to participate in the experiment
legal_age = 18

# estimated time to complete each maze
time_per_maze = 3

# the experiment memory format - the records is composed of two integer: maze_id, music_speed
# such that: maze_id = records[0]; music_speed = records[1]
maze_id_index = 0
music_speed_index = 1

# ___________ Folder and File Names _______________________________________#

# sub-folder names
maze_path = 'mazes/'
memory_path = 'conditions/'
image_path = "images/"
result_path = "results/"
detailed_result_path = "detailed_time_data/"
music_path = "music/"

# critical file names
memory_filename = 'experiment_memory.txt'
participant_id_filename = 'participant_ids.txt'
result_file = 'experiment_results.csv'

# image file names
player_img = "logo_smp_62.png"
wall_img = "block.png"
goal_img = "cup.png"
win_img = "win.png"
button_img = 'button.png'
UCL_img = 'UCL_logo.png'

# music file name and format
music_name = "Colin-opens-his-eyes"
music_format = "mp3"

# maze file name
maze_name = 'maze'

# individual detailed maze rime file name
maze_time_name = 'Maze_record'

# ___________ Menu Designs and Information Inputs _______________________________________#

# caption for the menu
menu_caption = 'UCL CoDes23/24 Music Maze Experiment'

# main menu caption
main_menu_caption = "UCL CoDes23/24 Music Maze"

# variables defined in the experiment
player_id = ['Subject_ID']
maze_vars = ['Maze_ID', 'Maze_speed', 'Time_elapsed']

demographics_list = ['age', 'gender', 'ethnicity', 'education', 'employment', 'topographical', 'auditory',
                     'attention', 'judgment', 'decision', 'interaction']

education = [("Less than high school degree", "Less than high school degree"),
             ("High school degree or equivalent", "High school degree or equivalent"),
             ("Some college but no degree", "Some college but no degree"),
             ("Bachelor's degree", "Bachelor's degree"),
             ("Master's degree", "Master's degree"),
             ("Doctoral degree", "Doctoral degree"),
             ("Doctor of Medicine", "Doctor of Medicine")]

gender = [("Female", "Female"), ("Male", "Male"),
          ("Trans woman", "Trans woman"), ("Trans man", "Trans man"),
          ("Non-binary", "Non-binary"), ("Queer", "Queer"),
          ("Other gender", "Other gender")]

employment = [("Student   ", "Student   "),
              ("Employed  ", "Employed  "),
              ("Unemployed", "Unemployed"),
              ("Retired   ", "Retired   ")]

ethnicity = [("African", "African"),
             ("Arab", "Arab"),
             ("Caribbean", "Caribbean"),
             ("Caucasian", "Caucasian"),
             ("East Asian", "East Asian"),
             ("Hispanic", "Hispanic"),
             ("Mixed", "Mixed"),
             ("South Asian", "South Asian"),
             ("Other ethnic group", "Other ethnic group")]

attention = [("Introvert", "Introvert"), ("Extrovert", "Extrovert")]
judgment = [("Intuition", "Intuition"), ("Sensing", "Sensing")]
decision = [("Feeling", "Feeling"), ("Thinking", "Thinking")]
interaction = [("Perceiving", "Perceiving"), ("Judging", "Judging")]

# ___________ Experiment Messages for Participants _______________________________________#

# messages for user interface
user_input = "Please provide the following information:"

welcome = "Welcome to the UCL CoDes23/24 Lab!"

instruction_1 = f"In this Psychological Game \nYou will guide a small leopard to exit {num_tests} small mazes"
instruction_2 = "Use arrow keys to control its movement"
instruction_3 = "And move it towards a shining chalice"
instruction_4 = "Hope you like the music. Good Luck!"

agreement = "I understand my rights and by clicking 'I AGREE', I agree to participate in the experiment."

acknowledge_text = "Well done! Are you ready for the next puzzle?"

end_text = f"Congratulations! You have successfully completed {num_tests} puzzles. Thank you for your participation."

consent_text = ("The Department of Psychology and Languages Sciences at the UCL supports the practice of protection "
                "of human \nparticipants in research. The following will provide you with information about the "
                "experiment that will help you in \ndeciding whether or not you wish to participate. If you have any "
                "reason why you should not participate, please inform the \nexperimenter and the study will "
                "end now.\n\n"
                f" Description: In this experiment you will play {num_tests} mazes. "
                f"A music will play during the maze game.\n"
                f"Each maze will likely take {time_per_maze} minutes to complete. Try to do your best to complete "
                f"each maze. Please note that:\n"
                "- Confidentiality: All information you provide will remain confidential. \n"
                "- Health : If during this study you do not feel comfortable, you may leave and your information will "
                "be discarded. \n"
                "- Feedback: When this study is complete you will be provided with the results and you can ask any "
                "questions. \n"
                "- Contact: If you have any questions concerning this study please feel free to contact us "
                "through phone or email. \n"
                "- Confirmation: Please click 'I AGREE' to indicate that you agree to participate in the experiment. \n"
                "- Disclaimer: Your participation is solicited, yet strictly voluntary. All information will be kept "
                "confidential.\n\n")

# ___________ Constants _______________________________________#

# colour definition for pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

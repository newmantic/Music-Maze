# To run the program, execute the main python file: run_maze.py

# Participants can use arrow keys to control the figure to exit a maze

# All aggregated experiment results will be saved under the \results; more fine-grained individual results will be saved under the sub-folder \results\detailed_time_data

# The default settings are stored in the file params.py under the sub-folder \src

# To run experiment on participants, set: maze_dev = False
# To test experiment for QA, set: maze_dev = True

# To run experiment on participants, set: music_on = True
# To establish benchmark without music, set: music_on = False

# Experimenters can modify the number of mazes each participant will solve by: num tests = n

# Experimenters can modify the ID of mazes to be tested by: maze ids = [1, 2, 3, ..., n]

# Experimenters can modify the speed of music to be tested by providing pre-recorded files: myMusic 1.mp3, myMusic 2.mp3,
myMusic 3.mp3 under the sub-folder \music

# Experimenters can modify the maze dimension (default 17) in terms of the number of blocks on each side of a maze to n, under the condition that n = 2 × m + 1, where m is an integer.

# Experimenters can modify the legal age to participate in the experiment with the format: legal_age = n

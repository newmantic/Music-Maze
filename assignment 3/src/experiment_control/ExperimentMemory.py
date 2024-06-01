"""
ExperimentMemory is to ensure an equal number of participants in each condition without assuming a specific number
of participants; it also does so without assuming that the program will be running on the computer continuously until
all subjects have participated; it would rely on some external records (i.e., a record file) to achieve this
the record file is updated each time the desired number of participants take the test and a new maze or a new speed must
 be applied
"""
import src.params
import os
import random


class ExperimentMemory:
    def __init__(self):
        self.memory_path = src.params.memory_path
        # experiment_memory.txt records all previous experiment conditions already tested
        self.record_file = self.memory_path + src.params.memory_filename
        self.participant_file = self.memory_path + src.params.participant_id_filename
        self.records = None
        self.ids = None
        # self.randomise_condition()

    # the file 'experiment_memory.txt' can be empty, in which case the class ExperimentDesign will write new designs
    @staticmethod
    def read_file(file):
        if os.path.isfile(file):
            # file exists, return record
            file = open(file, 'r')
            all_records = file.readlines()
            file.close()
            return all_records
        else:
            # no file exists, return an empty list
            ExperimentMemory.create_file(file)
            return []

    @staticmethod
    def create_file(file):
        file = open(file, 'w')
        file.write("\n")
        file.close()

    @staticmethod
    def least_item_dict(dict_):
        return min(dict_, key=dict_.get)

    # this is to check load an existent experiment design in 'experiment_memory.txt'
    # iit also loads the current experiment condition index to use a specified design from memory in case
    # the experiment condition index is less than the number of designs in its memory
    def record_check(self):
        all_records = self.read_file(self.record_file)
        # all_records is the records of already tested maze_id & music_speed combination
        if len(all_records) > 0:
            string_records = [memories.replace('\n', '') for memories in all_records]
            self.records = [[int(exp_index) for exp_index in memories.split(',')] for memories in string_records
                            if len(memories) > 0]
        else:
            self.records = []
        # print(self.records)

    def id_check(self):
        id_records = self.read_file(self.participant_file)
        if len(id_records) > 0:
            ids = [(id.replace('\n', '')) for id in id_records]
            self.ids = [int(id) for id in ids if id.isdigit()]
        else:
            self.ids = []

    # assign an id to a participant
    def id_assignment(self):
        # check id records
        self.id_check()
        if len(self.ids) > 0:
            return self.ids[-1]+1
        else:
            return 1

    # find the least occurred maze_id and music_speed
    def randomise_condition(self, current_id):
        # check records of experiment configurations
        self.id_check()
        # load the last participant's id
        if len(self.ids) > 0:
            last_id = self.ids[-1]
        # initiate a new id if this is the first participant
        else:
            last_id = 0
        self.record_check()
        if len(self.records) > 0:
            # count already tested maze_id & music_speed
            maze_ids_dict = dict.fromkeys(src.params.maze_ids, 0)
            music_speed_dict = dict.fromkeys(src.params.music_speed, 0)
            for condition in self.records:
                try:
                    # self.records is composed of two integer: maze_id, music_speed
                    maze_ids_dict[condition[src.params.maze_id_index]] += 1
                    music_speed_dict[condition[src.params.music_speed_index]] += 1
                except (ValueError, IndexError):
                    print("Index or Value error " + str(condition))
            music_speed = self.least_item_dict(music_speed_dict)
            # assign the least used maze to the participant if it's her first time
            if current_id != last_id:
                maze_id = self.least_item_dict(maze_ids_dict)
            # otherwise, need to avoid the maze that has been used previously
            else:
                # assert the lengths of maze record and player record match
                assert len(self.records) == len(self.ids)
                # find the indices of all mazes the current participant has done
                id_maze_indices = [i for i, x in enumerate(self.ids) if x == current_id]
                maze = [self.records[i][src.params.maze_id_index] for i in id_maze_indices]
                unused_maze_ids_dict = maze_ids_dict.copy()
                for used_maze in maze:
                    unused_maze_ids_dict.pop(used_maze, None)
                print('unused_maze_ids_dict', unused_maze_ids_dict)
                # if not empty, then play the least used one from unused maze
                if unused_maze_ids_dict:
                    maze_id = self.least_item_dict(unused_maze_ids_dict)
                # if it's empty - the player has played all mazes, pick the one with the least used
                # this should not happen as the experimenter should set the number of mazes equal to or greater than
                # the number of mazes that a participant is going to play
                else:
                    maze_id = self.least_item_dict(maze_ids_dict)
                    print("Same participant maze_id: ", maze_id)
        else:
            print('random experiment condition')
            maze_id = random.choice(src.params.maze_ids)
            music_speed = random.choice(src.params.music_speed)
        print(maze_id, music_speed)
        return maze_id, music_speed

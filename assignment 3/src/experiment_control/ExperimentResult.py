"""
ExperimentResult is to save results to a file with correct formats
It specifies all formats we need to convert the experiment results to standard and readable forms
"""
import src.params
import os.path


class ExperimentResult:
    def __init__(self):
        self.result_path = src.params.result_path
        self.detailed_result_path = self.result_path + src.params.detailed_result_path
        self.result_file = self.result_path + src.params.result_file
        self.memory_path = src.params.memory_path
        self.record_file = self.memory_path + src.params.memory_filename
        self.participant_file = self.memory_path + src.params.participant_id_filename
        self.columns = src.params.player_id + src.params.demographics_list + src.params.maze_vars
        self.results = []
        self.check_file()

    # to append information one at a time
    def append_results(self, value):
        self.results.append(str(value))

    def add_column_titles(self):
        file = open(self.result_file, 'w')
        file.write(','.join(self.columns))
        file.write("\n")
        file.close()

    # to check the file has desired columns for better readability
    def check_file(self):
        if os.path.isfile(self.result_file):
            file = open(self.result_file, 'r')
            all_records = file.readlines()
            # if  file is empty then append columns
            if len(all_records) == 0:
                file.close()
                self.add_column_titles()
        else:
            self.add_column_titles()

    # get multiple items from multiple selected menus
    @staticmethod
    def get_multi_selection(multi_tuple):
        # get the index of multiple selections
        items_index = range(len(multi_tuple[1]))
        # retrieve the multiple items from the menu
        print(multi_tuple[0])
        multiple_items = [multi_tuple[0][ind][0] for ind in items_index]
        # return a string
        return '/'.join(multiple_items)

    # structure the result in accordance with csv format
    def result_structuring(self, individual_id, maze_id, time_elapsed, music_tempo, demographics_data):
        demo_item = src.params.demographics_list
        self.append_results(individual_id)
        self.append_results(int(demographics_data[demo_item[0]]))
        self.append_results(demographics_data[demo_item[1]][0][0])
        self.append_results(self.get_multi_selection(demographics_data[demo_item[2]]))
        self.append_results(demographics_data[demo_item[3]][0][0])
        self.append_results(demographics_data[demo_item[4]][0][0])
        self.append_results(demographics_data[demo_item[5]])
        self.append_results(demographics_data[demo_item[6]])
        self.append_results(demographics_data[demo_item[7]][0][0])
        self.append_results(demographics_data[demo_item[8]][0][0])
        self.append_results(demographics_data[demo_item[9]][0][0])
        self.append_results(demographics_data[demo_item[10]][0][0])
        self.append_results(maze_id)
        self.append_results(music_tempo)
        self.append_results(round(time_elapsed[-1][0], 6))

    # to save results in multiple lines by appending new participants' results, one at a time
    def save_aggregated_results(self, individual_id, maze_id, time_elapsed, music_tempo, demographics_data):
        # structure the data in accordance with the defined csv format
        self.result_structuring(individual_id, maze_id, time_elapsed, music_tempo, demographics_data)
        file = open(self.result_file, 'a')
        file.write(','.join(self.results))
        file.write("\n")
        file.close()

    def save_individual_result(self, individual_id, maze_id, time_elapsed, music_tempo):
        file_name = (self.detailed_result_path + src.params.maze_time_name + '_PlayerID' + str(individual_id) +
                     '_MazeID' + str(maze_id) + '_MusicSpeed' + str(music_tempo) + '.csv')
        file = open(file_name, 'w')
        file.write("Time passed, x, y \n")
        for item in time_elapsed:
            for ii in item:
                file.write(str(ii) + ", ")
            file.write("\n")
        file.close()

    @staticmethod
    def append_file(file_nanme, record):
        file = open(file_nanme, "a")  # append results and records
        if isinstance(record, int):
            file.write(str(record) + "\n")
        elif len(record) >= 2:
            file.write(str(record[0]) + ", " + str(record[1]) + "\n")
        file.close()

    # to reset the results
    def reset(self):
        self.results = []


import time
from pygame import mixer
import src.params


class Music:
    def __init__(self, tempo=0):
        self.music_path = src.params.music_path
        self.music_file = None
        self.music_speed = tempo  # default no music
        self.music_vol = 0.1
        self.music_intro = 1  # 1 sec before showing game screen for music to set in
        self.start_music()

    def set_speed(self, speed):
        self.music_speed = speed

    def start_music(self):
        if self.music_speed > 0:
            self.music_file = (self.music_path + src.params.music_name + '_' + str(self.music_speed) + '.' +
                               src.params.music_format)
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.set_volume(self.music_vol)
            mixer.music.play()
            time.sleep(self.music_intro)

    @staticmethod
    def stop_music():
        mixer.music.stop()

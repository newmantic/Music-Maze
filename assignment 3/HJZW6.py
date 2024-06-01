from src.app import *
import src.params

if __name__ == "__main__":
    # block_size is the size of maze block in pixels; dim is the maze dimension of a square maze
    # maze_dev indicates whether it is for dev test (minimum difficulty maze) or real maze experiment (complex maze)
    # music_on indicates whether music should be on - music-off mode can be used to establish benchmarks
    theApp = MazeApp(src.params.block_size, src.params.dim, dev_test=src.params.maze_dev, music_on=src.params.music_on)
    theApp.maze_execute()


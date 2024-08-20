import os
from downloader import Downloader
from chord_analyser import ChordAnalyser

downloaded_song_path = Downloader("song").download()

chord_timestamps = ChordAnalyser(downloaded_song_path).analyse()

breakpoint()

print(chord_timestamps)

# clear tmp once we're finished

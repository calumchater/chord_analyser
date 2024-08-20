from chord_extractor.extractors import Chordino


class ChordAnalyser:

    def __init__(self, song_path):
        self.song_path = song_path

    def analyse(self):
        # Setup Chordino with one of several parameters that can be passed
        chordino = Chordino(roll_on=1)

        # add some try catching here

        # Run extraction
        return chordino.extract(self.song_path)

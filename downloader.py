from pytube import YouTube
from pytube.exceptions import VideoUnavailable


class Downloader:

    def __init__(self, song_url):
        song_url = "https://www.youtube.com/watch?v=R7gZ-ueMjx4"
        self.song_url = song_url

    def download(self):

        # Things to add:
        # file too big

        try:
            yt = YouTube(self.song_url)

        except VideoUnavailable:
            print(f"Video {self.song_url} is unavaialable, skipping.")
        else:
            print(f"Downloading video: {self.song_url}")
            song_path = (
                yt.streams.filter(only_audio=True).first().download(output_path="tmp")
            )
            return song_path

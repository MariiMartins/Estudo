import os
from pytube import YouTube, Playlist

FULL_PATH = os.path.abspath(".")
PLAYLIST_URL = input("Coloque a URL da Playlist: ")
playlist = Playlist(PLAYLIST_URL)

path = os.path.join(FULL_PATH, playlist.title)

if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url)
        print(f"Downloading {video.title}")

        video_path = os.path.join(path, f"{video.title}.mp4")
        if os.path.isfile(video_path):
            print("Video existente..")
            continue

        stream = video.stream.get_highest_resolution()
        stream.download(output_path=path)
        print("Download Completo")

    except Exception as e:
        print(f" Ocorreu um erro com o download do seu video: {e}")
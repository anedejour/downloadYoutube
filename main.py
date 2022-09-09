import os
from pytube import YouTube

def downloadYoutube():

    save_path = "C:/Users/berr/Downloads"
    link = "https://www.youtube.com/watch?v=McBXpTutopM"

    audio = YouTube(link).streams.filter(only_audio=True).first()

    download_audio = audio.download(save_path)

    base, ext = os.path.splitext(download_audio)
    new_file = base + ".mp3"
    os.rename(download_audio, new_file)

if __name__ == "__main__":
    downloadYoutube()






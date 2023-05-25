from pytube import YouTube


def download_video(video_url, save_folder=""):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        stream.download(save_folder)
        print("Download complete!")
    except Exception as e:
        print("Error:", str(e))

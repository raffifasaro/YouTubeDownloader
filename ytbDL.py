from pytube import YouTube


def download_video(video_url, location_path=None):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        if location_path is None:
            stream.download()
        else:
            stream.download(output_path=location_path)
        print("Download complete!")
    except Exception as e:
        print("Error:", str(e))

from tqdm import tqdm
from pytube import YouTube
import ffmpeg

videoUrl = input("Video URL=")
fps = input("FPS=")
hres = input("Horizontal Resolution=")
threaded = input("Run on multiple threads (y/n)=")
if(threaded.lower() == 'y'):
    threads = input("Thread count=")


print("WARNING: This will overwrite the existing file 'video.mp4' and any existing frames in 'frames'.")
continueInput = input("Continue? (y/n)=")

if continueInput != "y":
    exit()

# Download the video
if videoUrl != '':
    print("Downloading video...")
    yt = YouTube(videoUrl)
    video = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video.download(filename="video-raw.mp4")

    # Convert the video to a video with the correct FPS and resolution
    print("Converting video...")
    ffmpeg.input('video-raw.mp4').output('video.mp4', vf='fps=' + fps + ',' + 'scale=' + hres + ':-2').run()

# run convert_video.py
if threaded.lower() == 'y':
    import convert_video_threaded
    convert_video_threaded.fps = fps
    convert_video_threaded.maxThreads = threads
else:
    import convert_video
    convert_video.fps = fps

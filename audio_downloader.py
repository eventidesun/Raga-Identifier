import yt_dlp
import os

# Folder name for temporary use
output_folder = "raga_samples/Hamsadhwani"
os.makedirs(output_folder, exist_ok=True)

# List of YouTube urls - temporary use - updated the urls for every new audio files I wanted to download
youtube_urls = [
    "https://www.youtube.com/watch?v=D1s8TAvvmeU",
    "https://www.youtube.com/watch?v=K4BWMVBuc6c",
    "https://www.youtube.com/watch?v=EI7h0syNqdA",
]

# the download options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, 'clip%(autonumber)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(youtube_urls)

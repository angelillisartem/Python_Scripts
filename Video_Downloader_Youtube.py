# Install library "pytube" with [pip install pytube]
from pytube import YouTube

# Insert a directory, where u download your video!
directoryMacOS: str = " (for macOS use /Users/yourUser/yourDirectory) "

# Insert a Video Link to download
video = input(str("Insert video link: "))

# Take in input the directory
percorso = input(str("Insert directory where u want to download a video: " + directoryMacOS))

# Take the video link
yt = YouTube(video)

# Select best video Resolution
yd = yt.streams.get_highest_resolution()

# Download the video and insert in the directory
yd.download(percorso)

# Finish the program with a message "Complete the download video, thank you to use this Script"
exit("Complete the download video, thank you to use this Script!")

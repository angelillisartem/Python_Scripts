from pytube import YouTube #Install library "YouTube" with [pip install YouTube]

macos: str = " (for macOS use /Users/yourUser/yourDirectory) "

video = input(str("Insert video link to downalod: "))
percorso = input(str("Insert where do u want to downalod: " + macos))

yt = YouTube(video)
yd = yt.streams.get_highest_resolution()
yd.download(percorso)

exit("Done")
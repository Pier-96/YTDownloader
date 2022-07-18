from ast import arg
from pytube import YouTube

link = "https://www.youtube.com/watch?v=ZwKvb5ZQjzE"
yt = YouTube(link)

print("Titulo: ", yt.title)
print("Autor: ", yt.author)
print("Visitas: ", yt.views)

yd = yt.streams.get_audio_only()
yd.download('/mnt/c/Users/PieroOP/OneDrive/Escritorio/audios')

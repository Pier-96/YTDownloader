from ast import arg
from pytube import YouTube

# Añade tu link entre los ""
link = ""
yt = YouTube(link)

print("Titulo: ", yt.title)
print("Autor: ", yt.author)
print("Visitas: ", yt.views)

yd = yt.streams.get_audio_only()
# Añade tu path donde quieres guardar tus audios
yd.download('/mnt/c/Users/PieroOP/OneDrive/Escritorio/audios')

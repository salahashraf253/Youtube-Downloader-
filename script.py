from pytube import YouTube
import os
from pathlib import Path
links= []
link_to_download= ""
numberOfVideos=int(input("Enter the number of videos you want to download: "))

path_to_download_folder = str(os.path.join(Path.home(), r"")) #enter here the path that you want to save in it
    
for i in range(0,numberOfVideos):
    link_to_download=input("Enter link here: ")
    links.append(link_to_download)

for i in range(0,numberOfVideos):
    link_to_download =links[i]
    url = YouTube(link_to_download)
    print("downloading...."+str(i+1))
    video = url.streams.get_highest_resolution()
    
    video.download(path_to_download_folder)
    print("Downloaded! :)")

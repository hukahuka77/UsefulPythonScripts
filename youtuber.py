#This is for downloading youtube videos easily. If you'd like to download videos outside of youtube, consider the module yt-dlp
# importing the module 
from pytube import YouTube 
  
# where to save 
download_path = "C:/Users/Andrew/Desktop/Youtube" 

# link of the video to be downloaded 
link = input("What video would you like to download? Paste video link here:\n")

yt=YouTube(link)

#default resolution, should provide highest res available but hasn't worked in my experience
stream = yt.streams.get_highest_resolution()

#If you want to specify resolution, change it here:
myres = "480p"
stream = yt.streams.filter(res=myres).first()

#then download the vid
stream.download(output_path=download_path)

print(
f"""Downloaded successfully!
      
Title: {yt.title}
Folder: {download_path}
""")

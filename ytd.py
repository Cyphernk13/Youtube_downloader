from pytube import YouTube
link = input("Enter the video link: ")
video=YouTube(link)
download=video.streams.get_highest_resolution()
path=input(r'Enter the path where you want to download the video: ')
try:
    download.download(path)
    print("Your video has been successfully downloaded :)")
except:
    print("Sorry there seemed to be an error :(")
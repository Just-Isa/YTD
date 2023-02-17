from tkinter import *
from pytube import YouTube
import subprocess
from time import sleep
import glob, os
from moviepy.editor import *

mp4 = True
fileName = ""

def quit(self):
    self.destroy()
    exit()

def selectMP4():
    global mp4 
    mp4 = True

def selectMP3():
    global mp4 
    mp4 = False

def convertToMp3(file, bytesize):
    global fileName
    sleep(2)
    for file in os.listdir("./downloads/mp3/"):
        video = AudioFileClip(r"./downloads/mp3/"+file)
        video.write_audiofile("./downloads/mp3/"+file.replace(".mp4",".mp3"))
        os.remove(r"./downloads/mp3/"+file)

def download():
    global mp4, fileName
    try:
        if mp4:
            url = YouTube(str(link.get()))
            video = url.streams.filter(file_extension="mp4").get_highest_resolution()
            video.download(output_path="./downloads/mp4")
            
            Label(root, 
                text="Video -> "+ video.title ,
                bg="#53599A", 
                font="arial 15").place(
                    x=100, 
                    y=100)
        else:
            url = YouTube(str(link.get()), on_complete_callback=convertToMp3)
            video = url.streams.filter(only_audio=True).first()
            video.download(output_path="./downloads/mp3")
            fileName = url.title
            
            Label(root, 
                text="Audio -> "+ video.title ,
                bg="#53599A", 
                font="arial 15").place(
                    x=100, 
                    y=100)
                
    except ValueError:
        Label(
            root, 
            text='Check Link!', 
            bg="#53599A",
            fg="#F87666", 
            font="arial 15").place(
                x=250, 
                y=80, 
                anchor="center")
        pass
    

root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("Downloader")
root.configure(background="#53599A")

# LINK
Label(root, text="Link", bg="#53599A", font='sans-serif 20 bold').place(x=250, y=120, anchor="center")

# DOWNLOAD BUTTON
downloadButton = Button(root, bg="#53599A", fg="#AEECEF", text = "Download", command=download)
downloadButton.place(x=250, y=250, anchor="center")

# INPUT FIELD
link = StringVar()
link_enter = Entry(root, width=50, bg="#6D9DC5", textvariable=link).place(x=250, y=200, anchor="center")

# RADIO BUTTONS
mp4 = Radiobutton(root, text="mp4", bg="#53599A", fg="black", font='sans-serif 15 bold', value=1, command=selectMP4).place(x=200, y=325, anchor="center")
mp3 = Radiobutton(root, text="mp3", bg="#53599A", fg="black", font='sans-serif 15 bold', value=2, command=selectMP3).place(x=300, y=325, anchor="center")

Button(root, text="Quit", command=lambda root=root:quit(root)).place(x=250, y=400, anchor="center")


root.mainloop()
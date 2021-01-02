# Python audiobook project

# This project is done by: Md. Fahim Bin Amin

from tkinter import *   # Importing the GUI named tkinter


def close_window():
    root.destroy()  # Destroying the main window

 # Creating the tkinter window 


root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text="Browse and select the PDF file you want to process.", fg="blue", command=close_window)  # The window will get closed by the command
redbutton.pack( side = LEFT)


# Adding widget to the root window

Label(root, text='FBA Project: Audiobook', font=('Comic Sans MS', 25)).pack(side=TOP, pady=10)
# other stylish fonts can be used here too

photo = PhotoImage(file=r"C:\\Users\\FBA Desktop\\Downloads\\AudiobookGUICanvas.gif")  # Creating a photoimage object to use image . JPEG wouldn't work here
Button(root, image=photo).pack(side=TOP)  # Setting image in button
root.mainloop()

# Executing the command for text to speech

import pyttsx3
import PyPDF2
engine = pyttsx3.init()  # Object creation
rate = engine.getProperty('rate')
print (rate)  # Printing the current voice rate
engine.setProperty('rate', 185)   # Setting up the new voice rate
volume = engine.getProperty('volume')
print (volume)  # Printing the current volume level
engine.setProperty('volume',1.0)  # Setting up the volume level between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
from tkinter.filedialog import *
book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()
engine.save_to_file(text, 'Audiobook created by FBA.mp3')   # Saving the voice to a file 
engine.runAndWait()
print("Your audiobook file has been generated as an mp3 file. Check the project file directory for getting the file.")

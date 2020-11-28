from tkinter import *
def close_window():
    root.destroy()
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text="Browse and select the PDF file you want to process.", fg="blue", command=close_window)
redbutton.pack( side = LEFT)
Label(root, text='FBA Project: Audiobook', font=('Comic Sans MS', 25)).pack(side=TOP, pady=10)
photo = PhotoImage(file=r"C:\\Users\\FBA Desktop\\Downloads\\book.gif")
Button(root, image=photo).pack(side=TOP)
root.mainloop()
import pyttsx3
import PyPDF2
engine = pyttsx3.init()
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 185)
volume = engine.getProperty('volume')
print (volume)
engine.setProperty('volume',1.0)
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
engine.save_to_file(text, 'Audiobook created by FBA.mp3')
engine.runAndWait()
print("Your audiobook file has been generated as an mp3 file. Check the project file directory for getting the file.")

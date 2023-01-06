import tkinter as tk
from fileGenerator import FileGenerator
import os

window=tk.Tk()
window.minsize(300,300)
window.maxsize(300,300)
window.title("Practo")
# Input For name of output file
outFile=tk.StringVar()
outFileLabel=tk.Label(window,text="Enter Output File Name ",font=(20),pady=10,padx=10)
outFileLabel.place(x=0,y=0)
outFileInput=tk.Entry(window,width=30,textvariable=outFile).place(y=12,x=180)

# Radio Button for Extention
language=tk.StringVar(value=" ")
radioLabel=tk.Label(window,text="Select Code Language ",font=(20),pady=10,padx=10)
radioLabel.place(x=0,y=50)
python=tk.Radiobutton(window,text="Python",variable=language,value="py",padx=10,font=20)
python.place(x=0,y=80)
cpp=tk.Radiobutton(window,text="C++",variable=language,value="cpp",padx=10,font=20)
cpp.place(x=0,y=100)

# Start Button
def start() -> None:
    window.destroy()
    baseFileName = os.path.basename(__file__)
    object=FileGenerator()
    object.ignoreList.add(baseFileName)
    object.outputFileName=outFile.get()
    object.extension=language.get()
    object.start()

startButton=tk.Button(window,text="Start Practo",command=start)
startButton.place(x=100,y=200)
window.mainloop()
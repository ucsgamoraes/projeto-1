import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

labelText = tk.StringVar()
labelText.set("Ingredientes: ")
labelDir = tk.Label(frame, textvariable=labelText, height=4).place(x=5, y=0)
inputtxt = tk.Text(frame,height = 1,width = 15)
inputtxt.pack(padx=5, pady=15, side=tk.LEFT)

  
# Button Creation
printButton = tk.Button(frame,text = "Print", command = printInput)
printButton.pack()
  
# Label Creation
frame.mainloop()
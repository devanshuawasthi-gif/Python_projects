#----> DIGITAL CLOCK --->

import time

import tkinter as tk

root = tk.Tk()
root.title("Digital clock Standard")

def currentTime():
    
    #find current time and display it in the clock
    # update the time in everry 1000 milisecond
    string = time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,currentTime)
    
    
label = tk.Label(
    root,
    font=('calibri',60,'bold'),
    background='yellow',
    foreground='black'
)

label.pack(anchor="center")

currentTime()

root.mainloop()




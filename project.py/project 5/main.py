####---->  PHOTO ALBUM  --> 

import tkinter as tk
import time
from PIL import Image, ImageTk

#Main application window

root = tk.Tk()
root.title("Photo  slideshow album")
root.geometry("900x900")

# list of image path

image_paths =[
    r"C:\Users\Devansh\OneDrive\Desktop\albumpy/1.image",
    r"C:\Users\Devansh\OneDrive\Desktop\albumpy/2.image",
    r"C:\Users\Devansh\OneDrive\Desktop\albumpy/3.image",
    r"C:\Users\Devansh\OneDrive\Desktop\albumpy/4.image",
    r"C:\Users\Devansh\OneDrive\Desktop\albumpy/5.image",
]

image_size= (700, 700)
images= []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)
    
    
# convert pil image to tkinter comaptible image 

final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)
    
    
# label widget to keep photoo

image_label= tk.Label(root)
image_label.pack(pady=30)


# --> slideshow function

def start_slideshow():
    for photo in final_images:
        image_label.config(image= photo)
        image_label.image= photo
        root.update()
        time.sleep(2)
        
        
#--. button --.

play_button= tk.Button(
    root,
    text= "play the sludeshow",
    font=("Arial", 17),
    commmand=start_slideshow
)
play_button.pack(pady=40)

root.mainloop()
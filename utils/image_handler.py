import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


class Image_Handler:
    def __init__(self) -> None:
        icons_path = os.path.join('data', 'icons')
        icons_list = os.listdir(icons_path)
        self.icons_dict = {}
        for icon in icons_list:
            name = icon.split("_")[0]
            icon = os.path.join(icons_path, icon)
            self.icons_dict.update({name: icon})


    def get_icon_list(self) -> dict:
        return self.icons_dict


    def get_icon(self, name: str, width: int = None, height: int = None) -> ImageTk.PhotoImage:
        image = Image.open(self.icons_dict[name])

        if width or height:
            image = self.resize_image(image=image, width=width, height=height)

        return ImageTk.PhotoImage(image)
        


    def resize_image(self, image: Image, width: int, height: int) -> Image:
        
        resized_image = image.resize((width, height))

        return resized_image
    

if __name__ == "__main__":

    root = tk.Tk()

    img_h = Image_Handler()
    print(img_h.get_icon_list())
    data = img_h.get_icon("game", 100, 100)

    button_image = tk.Button(root, image=data, command=lambda: print('Button clicked!'))
    # button_image.image = data  # Keep a reference to the PhotoImage object
    button_image.pack() 

    root.mainloop()
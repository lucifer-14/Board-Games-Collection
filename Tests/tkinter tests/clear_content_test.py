# import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

# Define the main menu function
def main_menu():
    # Define the content of the main menu
    label = ttk.Label(root, text="Main Menu", font=("Arial", 24))
    label.pack()

    # Add buttons or menu items to change the content
    button1 = ttk.Button(root, text="Show Page 1", command=show_page1)
    button1.pack()

    button2 = ttk.Button(root, text="Show Page 2", command=show_page2)
    button2.pack()

# Function to show Page 1 content
def show_page1():
    # Clear previous content
    clear_content()

    # Add content for Page 1
    label = ttk.Label(root, text="Page 1 Content", font=("Arial", 24))
    label.pack()

# Function to show Page 2 content
def show_page2():
    # Clear previous content
    clear_content()

    # Add content for Page 2
    label = ttk.Label(root, text="Page 2 Content", font=("Arial", 24))
    label.pack()

# Function to clear previous content
def clear_content():
    for widget in root.winfo_children():
        widget.pack_forget()

# Display the main menu
main_menu()

root.mainloop()
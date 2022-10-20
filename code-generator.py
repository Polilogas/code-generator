# importing the module tkinter
from distutils.cmd import Command
from operator import length_hint
import tkinter as tk
from tkinter import Checkbutton, ttk
import random
import string
from turtle import width
from unittest import result


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the root window
        self.title("Code Generator")
        self.geometry("500x300")

        # Check box for lowrcase
        self.checkvar1 = tk.IntVar()
        self.lowecaseCheckBox = Checkbutton(self, text="lowrcase", variable=self.checkvar1)
        self.lowecaseCheckBox.pack() 

        # Check box for UPPERCASE
        self.checkvar2 = tk.IntVar()
        self.UPPERCASECheckBox = Checkbutton(self, text="UPPERCASE", variable=self.checkvar2)
        self.UPPERCASECheckBox.pack() 

        # Check box for numbers
        self.checkvar3 = tk.IntVar()
        self.numbersCheckBox = Checkbutton(self, text="0123456789", variable=self.checkvar3)
        self.numbersCheckBox.pack() 

        # Check box for symbols
        self.checkvar4 = tk.IntVar()
        self.symbolsCheckBox = Checkbutton(self, text="!@#$%^&*()", variable=self.checkvar4)
        self.symbolsCheckBox.pack() 

        # Button
        self.button = ttk.Button(self, text="Click Me")
        self.button['command'] = self.generateCode
        self.button.pack()

        # Label
        self.password = ttk.Label(self, text="")
        self.password.pack()

    def generateCode(self):
        if self.checkvar1.get() == 1:
            letters = string.ascii_lowercase
            result = ''.join(random.choice(letters) for i in range(5))
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()


    
        
        return "asdasdf"


if __name__ == "__main__":
    app = App()
    app.mainloop()

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

    # It generates a code pased on the inputes, when the button is clicked.
    def generateCode(self):
        # If Lowercase, Uppercase, Numbers and Symbis are not selected
        if self.checkvar1.get() == 0 and self.checkvar2.get() == 0 and self.checkvar3.get() == 0 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Symbols is selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 0 and self.checkvar3.get() == 0 and self.checkvar4.get() == 1:
            checkBoxes = string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Numbers is selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 0 and self.checkvar3.get() == 1 and self.checkvar4.get() == 0:
            checkBoxes = string.digits
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Numbers and Symbols are selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 0 and self.checkvar3.get() == 1 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Uppercase is selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 1 and self.checkvar3.get() == 0 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_uppercase
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Uppercase and Symbols are selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 1 and self.checkvar3.get() == 0 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_uppercase + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Uppercase and Numbers are selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 1 and self.checkvar3.get() == 1 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Uppercase, Numbers and Symbols are selected
        elif self.checkvar1.get() == 0 and self.checkvar2.get() == 1 and self.checkvar3.get() == 1 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_uppercase + string.digits + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase is selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 0 and self.checkvar3.get() == 0 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_lowercase
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase and Symbols are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 0 and self.checkvar3.get() == 0 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_lowercase + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase and Numbers are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 0 and self.checkvar3.get() == 1 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_lowercase + string.digits
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase, Numbers and Symbols are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 0 and self.checkvar3.get() == 1 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_lowercase + string.digits + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase and Uppercase are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 1 and self.checkvar3.get() == 0 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase, Uppercase and Symbols are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 1 and self.checkvar3.get() == 0 and self.checkvar4.get() == 1:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase, Uppercase and Numbers are selected
        elif self.checkvar1.get() == 1 and self.checkvar2.get() == 1 and self.checkvar3.get() == 1 and self.checkvar4.get() == 0:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase + string.digits
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()

        # If Lowercase, Uppercase, Numbers and Symbols are selected
        else:
            checkBoxes = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            result = ''.join(random.choice(checkBoxes) for i in range(5))  # range is for the lenght
            self.password.destroy()
            self.password = ttk.Label(self, text=result)
            self.password.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()

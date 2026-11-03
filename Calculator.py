# Calculator in Python v1.0

import tkinter as tk


class Calculator:

    def __init__(self, finestra):

        self.window = finestra
        self.title = "Py Calculator"
        self.background_color = "#34037d"

        self.window.title(self.title)
        self.window.configure(bg=self.background_color)
        self.window.geometry("400x600")

        self.create_display()
        self.keys()

    def create_display(self):

        self.display = tk.Entry(
            self.window,
            font=("Arial", 32),
            bg="#34037d",
            fg="white",
            justify="right",
            borderwidth=0
        )

        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=15,
            pady=20
        )

    def keys(self):

        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                button = tk.Button(
                    self.window,
                    text=text,
                    font=("Arial", 20),
                    bg="#000000",
                    fg="white"
                )

                button.grid(row=r+1, column=c, sticky="nsew")


interface = tk.Tk()

app = Calculator(interface)

for i in range(4):
    interface.grid_columnconfigure(i, weight=1)

for i in range(6):
    interface.grid_rowconfigure(i, weight=1)

tk.mainloop()
# Calculator in Python V1.4

import tkinter as tk

class Calculator:

    def __init__(self, finestra):

        # Configurazione finestra
        self.window = finestra
        self.title = "Py Calculator"
        self.background_color = "#34037d"

        self.window.title(self.title)
        self.window.configure(bg=self.background_color)
        self.window.geometry("400x600")
        self.window.resizable(False, False)

        # Memoria dei calcoli
        self.first_number = None
        self.operator = None

        # Creazione interfaccia
        self.create_display()
        self.keys()

    # DISPLAY
    def create_display(self):

        self.display = tk.Entry(
            self.window,
            font=("Arial", 32),
            bg="#34037d",
            fg="white",
            justify="" \
            "right",
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

    # TASTIERA
    def keys(self):

        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                # Scelta dell'azione del pulsante
                if text == "C":
                    action = self.clear_display

                elif text == "=":
                    action = self.calculate

                elif text in ["+", "-", "×", "÷"]:
                    action = lambda value=text: self.set_operator(value)

                elif text == "±":
                    action = self.change_sign

                elif text == "%":
                    action = self.percentage

                else:
                    action = lambda value=text: self.write_number(value)

                # Creazione pulsante
                button = tk.Button(
                    self.window,
                    text=text,
                    font=("Arial", 20),
                    bg="#000000",
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white",
                    borderwidth=0,
                    command=action
                )

                button.grid(
                    row=r + 1,
                    column=c,
                    sticky="nsew",
                    padx=3,
                    pady=3
                )

    # INSERIMENTO NUMERI
    def write_number(self, value):

        current = self.display.get()

        if value == "." and "." in current:
            return

        if current == "Errore":
            self.display.delete(0, tk.END)

        self.display.insert(tk.END, value)

    # CANCELLA DISPLAY
    def clear_display(self):

        self.display.delete(0, tk.END)
        self.first_number = None
        self.operator = None

    # CAMBIO SEGNO
    def change_sign(self):

        try:
            number = float(self.display.get())
            number = -number

            self.display.delete(0, tk.END)
            self.display.insert(0, str(number))

        except ValueError:
            pass

    # PERCENTUALE
    def percentage(self):

        try:
            number = float(self.display.get())
            result = number / 100

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except ValueError:
            pass

    # MEMORIZZAZIONE OPERATORE
    def set_operator(self, operator):

        try:
            self.first_number = float(self.display.get())
            self.operator = operator

            self.display.delete(0, tk.END)

        except ValueError:
            pass

    # CALCOLO
    def calculate(self):

        try:
            second_number = float(self.display.get())

            if self.first_number is None or self.operator is None:
                return

            if self.operator == "+":
                result = self.first_number + second_number

            elif self.operator == "-":
                result = self.first_number - second_number

            elif self.operator == "×":
                result = self.first_number * second_number

            elif self.operator == "÷":

                if second_number == 0:
                    raise ZeroDivisionError

                result = self.first_number / second_number

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

            # Reset della memoria
            self.first_number = None
            self.operator = None

        except ZeroDivisionError:

            self.display.delete(0, tk.END)
            self.display.insert(0, "Errore")

            self.first_number = None
            self.operator = None

        except ValueError:
            pass


# AVVIO PROGRAMMA

finestra = tk.Tk()

app = Calculator(finestra)

# Ridimensionamento automatico celle
for i in range(4):
    finestra.grid_columnconfigure(i, weight=1)

for i in range(6):
    finestra.grid_rowconfigure(i, weight=1)

# Avvio interfaccia
finestra.mainloop()
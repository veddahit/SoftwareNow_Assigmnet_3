

# git link    https://github.com/veddahit/SoftwareNow_Assigmnet_3/blob/main/qn1.py

import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculator")

        # Entry widget to display and input values
        self.entry = tk.Entry(self, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create and place buttons on the grid
        for (text, row, column) in buttons:
            btn = CalculatorButton(self, text=text)
            btn.grid(row=row, column=column)

    # Method overriding - Customizing the behavior of the close button
    def destroy(self):
        print("Closing the calculator app.")
        super().destroy()

# Encapsulation - Wrapping the Tkinter Button with a custom class
class CalculatorButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(
            width=4,
            height=2,
            font=('Arial', 16),
            command=self.on_button_click
        )

    # Polymorphism - This method can be overridden by specific buttons
    def on_button_click(self):
        current_text = app.entry.get()
        button_text = self.cget('text')

        if button_text == 'C':
            app.entry.delete(0, tk.END)
        elif button_text == '=':
            try:
                result = eval(current_text)
                app.entry.delete(0, tk.END)
                app.entry.insert(tk.END, str(result))
            except Exception as e:
                app.entry.delete(0, tk.END)
                app.entry.insert(tk.END, "Error")
        else:
            app.entry.insert(tk.END, button_text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

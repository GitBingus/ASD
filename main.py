import os
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter App")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="CCP PMS")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")


gui = App()
gui.mainloop()
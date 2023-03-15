from tkinter import Button, Label, PhotoImage, Tk
from src import settings
from src.directorymenu import DirectoryMenu


class MainMenu(object):
    def __init__(self):
        self.window: Tk = Tk()

        self.background_image: PhotoImage = PhotoImage(file="images/background.png")
        self.background_label: Label = Label(self.window, image=self.background_image)

        self.text: Label = Label(self.window, text="Kliknij aby rozpocząć pobieranie.", font=settings.font)
        self.start_button: Button = Button(self.window, text="Rozpocznij", font=settings.font, command=self.start)

        self.create_menu()
        self.window.mainloop()

    def start(self):
        self.background_label.destroy()
        self.text.destroy()
        self.start_button.destroy()

        DirectoryMenu(window=self.window)

    def create_menu(self):
        self.window.geometry("500x500")
        self.window.resizable(width=False, height=False)
        self.window.title("Pobieracz YT")
        self.background_label.place(x="0", y="0")
        self.text.place(x="75", y="250", width="350", height="50")
        self.start_button.place(x="112.5", y="350", width="275", height="50")


if __name__ == '__main__':
    gui: MainMenu = MainMenu()

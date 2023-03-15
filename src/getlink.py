from tkinter import Button, Label, PhotoImage, Tk, messagebox, Entry
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from src.confirm import Confirm
from src import settings


class GetLinkMenu(object):
    def __init__(self, path: str, window_old: Tk):
        self.link = None
        self.path: str = path

        self.window: Tk = window_old

        self.background_image: PhotoImage = PhotoImage(file="images/background.png")
        self.background_label: Label = Label(self.window, image=self.background_image)

        self.input_box: Entry = Entry(font=settings.font, bg=settings.bg_text)
        self.text: Label = Label(self.window, text="Podaj link do filmu YouTube:", font=settings.font)
        self.confirm_button: Button = Button(self.window, text="Zatwierdź", font=settings.font, command=self.get_link)

        self.create_menu()

    def check_link(self):
        try:
            video: YouTube = YouTube(url=self.link)
            self.background_label.destroy()
            self.input_box.destroy()
            self.text.destroy()
            self.confirm_button.destroy()

            Confirm(video=video, path=self.path, window=self.window)
        except RegexMatchError:
            messagebox.showerror("Zły link", "Nie znaleziono filmu o podanym linku!")

    def get_link(self):
        self.link = self.input_box.get()
        if self.link != "":
            if self.link.startswith("https://"):
                self.check_link()
            else:
                messagebox.showerror("Nieprawidłowy link", "Link musi zaczynać się od https://")
        else:
            messagebox.showerror("Brak linku", "Nie podałeś linku")

    def recreate(self):
        self.create_menu()
        self.window.mainloop()

    def create_menu(self):
        self.window.title("Podawanie linku")
        self.input_box.place(x="25", y="270", width="450", height="50")
        self.confirm_button.place(x="190", y="330", width="120", height="50")
        self.background_label.place(x="0", y="0")
        self.text.place(x="25", y="255", width="450")

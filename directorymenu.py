from tkinter import Button, StringVar, Label, PhotoImage, Tk
from tkinter import filedialog, messagebox
from getlink import GetLinkMenu
import settings


class DirectoryMenu(object):
    def __init__(self, window: Tk):
        self.path = None

        self.window: Tk = window

        self.background_image: PhotoImage = PhotoImage(file="images/background.png")
        self.background_label: Label = Label(self.window, image=self.background_image)

        self.path_button: Button = Button(
            self.window, text="Otwórz eksplolator", font=settings.font, command=self.file_explorer)
        self.confirm_button: Button = Button(self.window, text="Potwierdź", font=settings.font, command=self.confirm)
        self.current_path: StringVar = StringVar()
        self.text: Label = Label(self.window, textvariable=self.current_path, font=settings.font, bg=settings.bg_text)

        self.update_text()
        self.create_menu()

    def confirm(self):
        if self.path:
            self.background_label.destroy()
            self.path_button.destroy()
            self.confirm_button.destroy()
            self.text.destroy()
            GetLinkMenu(path=self.path, window_old=self.window)
        else:
            messagebox.showerror("Błąd", "Nie podano ścieżki")

    def update_text(self):
        self.current_path.set("Musisz wybrać miejsce zapisu swojego filmu."
                              "\nKliknij przycisk po niżej aby wybrać folder"
                              "\nAktualna scieżka:\n"
                              f"{self.path if self.path else 'Nie podano'}")

    def file_explorer(self):
        self.path = filedialog.askdirectory()
        self.update_text()

    def create_menu(self):
        self.window.title("Wybieranie miejscu zapisu")
        self.background_label.place(x="0", y="0")
        self.text.place(x="0", y="170", width="500", height="150")
        self.path_button.place(x="15", y="400", width="230", height="50")
        self.confirm_button.place(x="250", y="400", width="230", height="50")

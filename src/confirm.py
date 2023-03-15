from tkinter import Button, Label, PhotoImage, Tk, StringVar
from pytube import YouTube
from threading import Thread
from src import settings
from typing import List


class Confirm(object):
    def __init__(self, path: str, video: YouTube, window: Tk):
        self.video: YouTube = video
        self.path: str = path

        self.window: Tk = window

        self.background_image: PhotoImage = PhotoImage(file="images/background.png")
        self.background_label: Label = Label(self.window, image=self.background_image)
        self.checking_image: PhotoImage = PhotoImage(file="images/checking.png")
        video_tittle: List[str] = \
            [j + '\n' for j in [self.video.title[i:i+37] for i in range(0, len(self.video.title), 37)]]
        self.text: Label = Label(text=f"Tytuł: {''.join(video_tittle)}Autor: {self.video.author}\n", font=settings.font)
        self.confirm_button: Button = Button(self.window, text="Pobierz", font=settings.font,
                                             command=self.ready_to_download)
        self.cancel_button: Button = Button(self.window, text="Anuluj", font=settings.font, command=self.close)

        self.status_display: StringVar = StringVar()
        self.checking_label: Label = Label(self.window, image=self.checking_image)
        self.status: Label = Label(self.window, textvariable=self.status_display, font=settings.font)

        self.done_button: Button = Button(self.window, text="Zamknij", font=settings.font, command=self.close)

        self.create_menu()

    def close(self):
        self.window.destroy()
        exit()

    def destroy_self(self):
        self.confirm_button.destroy()
        self.text.destroy()
        self.cancel_button.destroy()

    def ready_to_download(self):
        self.confirm_button.destroy()
        self.text.destroy()
        self.cancel_button.destroy()

        self.window.title("Pobieranie")
        self.status.place(x="25", y="100", width="450", height="60")
        self.checking_label.place(x="25", y="120", width="450", height="450")

        download_thread: Thread = Thread(target=self.download_video)
        download_thread.start()
        self.status_display.set("Pobieranie, czekaj...")

    def download_video(self):
        downloader = self.video.streams.get_highest_resolution()
        downloader.download(self.path)

        self.checking_label.destroy()
        self.status_display.set("Gotowe. Możesz zamknąć okno!")
        self.done_button.place(x="112.5", y="350", width="275", height="50")
        
    def create_menu(self):
        self.window.title("Potwierdzanie")
        self.background_label.place(x="0", y="0")
        self.text.place(x="0", y="100", width="500", height="350")
        self.confirm_button.place(x="15", y="400", width="230", height="50")
        self.cancel_button.place(x="250", y="400", width="230", height="50")

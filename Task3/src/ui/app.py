from tkinter import Tk
from .frames.MainFrame import MainFrame


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__width = 1000
        self.__height = 800

        self.title("Painting Style Recognition")
        self.center_window()

        self.main_frame = MainFrame()
        self.main_frame.pack()

    def center_window(self) -> None:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (self.__width / 2))
        y = int((screen_height / 2) - (self.__height / 2))

        self.geometry(f"{self.__width}x{self.__height}+{x}+{y}")
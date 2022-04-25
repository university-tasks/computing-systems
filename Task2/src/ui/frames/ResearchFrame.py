import os
from tkinter import (
    HORIZONTAL,
    N,
    W,
    Button,
    Canvas,
    Entry,
    Frame,
    Label,
    OptionMenu,
    Scrollbar,
    StringVar,
)
from typing import Callable
from PIL import ImageTk, Image
from ...core.configuration import DATA_PATH, DATABASE_CONF
from ...core.features import features
from ...core.research import research


class ResearchFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__state = {
            "database": StringVar(self, list(DATABASE_CONF.keys())[0]),
            "method": StringVar(self, list(features.keys())[0]),
            "train_count": StringVar(self, 3)
        }

        self.tools_frame = Frame(self)
        self.canvas_frame = Frame(self)

        self.tools_frame.grid(column="0", row="0", sticky=W)
        self.canvas_frame.grid(column="1", row="0", sticky=W)

        self.database_dropdown()
        self.method_dropdown()
        self.train_count_entry()
        self.run_button()
        self.graphics()

    def graphics(self) -> None:
        self.canvas = Canvas(self.canvas_frame, width=600, height=400, bg="#CACACA")

        # Scroll
        self.scroll_x = Scrollbar(self, orient=HORIZONTAL, command=self.canvas.xview)

        self.columnconfigure(0, weight=1)
        self.canvas.config(xscrollcommand=self.scroll_x.set, scrollregion=self.canvas.bbox("all"))

        self.canvas.create_window((0, 0), window=self, anchor=N + W)
        self.canvas.pack()

    def database_dropdown(self) -> None:
        self.__dropdown(
            self.tools_frame,
            "Database",
            self.__state["database"],
            list(DATABASE_CONF.keys()),
        )

    def method_dropdown(self) -> None:
        self.__dropdown(self.tools_frame, "Method", self.__state["method"], list(features.keys()))

    def train_count_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["train_count"], "Train Count")

    def run_button(self) -> None:
        self.__button(self.tools_frame, self.run_research, "Run Research")

    def __entry(self, frame: Frame, var: StringVar, label: str = "") -> None:
        Label(frame, text=label).pack()
        Entry(frame, textvariable=var).pack()

    def __dropdown(self, frame: Frame, label: str, var: StringVar, options: list) -> None:
        Label(frame, text=label).pack()
        OptionMenu(frame, var, *options).pack()

    def __button(self, frame: Frame, command: Callable, title="button", width=None, height=None) -> None:
        button = Button(frame, text=title, width=width, height=height, command=command)
        button.pack()

    def run_research(self) -> None:
        self.canvas.delete("all")
        best_scores, _, _ = research(self.__state["database"].get(), self.__state["method"].get(), int(self.__state["train_count"].get()))
        self.result_images = []

        print(f"BEST SCORES: {best_scores}")

        image = Image.open(os.path.join(DATA_PATH, "results", "result_1_n.png"))
        image = image.resize((500, 300))
        image = ImageTk.PhotoImage(image)
        self.result_images.append(image)
        self.canvas.create_image(300, 250, image=image)

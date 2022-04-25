import random
from os import path
from tkinter import W, Button, Canvas, Entry, Frame, Label, OptionMenu, StringVar
from typing import Callable
from PIL import ImageTk, Image
from ...core.configuration import DATABASE_CONF, DATA_PATH
from ...core.features import features
from ...core.recognition import parallel_recognition


class ParallelFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__state = {
            "database": StringVar(self, list(DATABASE_CONF.keys())[0]),
            "histogram": StringVar(),
            "scale": StringVar(),
            "gradient": StringVar(),
            "dft": StringVar(),
            "dct": StringVar(),
            "train_count": StringVar(),
            "result_images": [],
        }

        self.tools_frame = Frame(self)
        self.canvas_frame = Frame(self)

        self.canvas = Canvas(self.canvas_frame, width=1000, height=1000, bg="#CACACA")

        self.tools_frame.grid(column="0", row="0", sticky=W)
        self.canvas_frame.grid(column="1", row="0", sticky=W)

        self.database_dropdown()
        self.histogram_entry()
        self.scale_entry()
        self.gradient_entry()
        self.dft_entry()
        self.dct_entry()
        self.train_count_entry()
        self.run_button()
        self.canvas.pack()

    def database_dropdown(self) -> None:
        self.__dropdown(
            self.tools_frame,
            "Database",
            self.__state["database"],
            list(DATABASE_CONF.keys()),
        )

    def histogram_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["histogram"], "Histogram")

    def scale_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["scale"], "Scale")

    def gradient_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["gradient"], "Gradient")

    def dft_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["dft"], "DFT")

    def dct_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["dct"], "DCT")

    def train_count_entry(self) -> None:
        self.__entry(self.tools_frame, self.__state["train_count"], "Train Count")

    def run_button(self) -> None:
        self.__button(self.tools_frame, self.parallel_experiment, "Run Recognition")

    def __entry(self, frame: Frame, var: StringVar, label: str = "") -> None:
        Label(frame, text=label).pack()
        Entry(frame, textvariable=var).pack()

    def __dropdown(self, frame: Frame, label: str, var: StringVar, options: list) -> None:
        Label(frame, text=label).pack()
        OptionMenu(frame, var, *options).pack()

    def __button(
        self,
        frame: Frame,
        command: Callable,
        title="button",
        width: int = None,
        height: int = None,
    ) -> None:
        button = Button(frame, text=title, width=width, height=height, command=command)
        button.pack()

    def parallel_experiment(self) -> None:
        params = [
            ("histogram", int(self.__state["histogram"].get())),
            ("scale", int(self.__state["scale"].get())),
            ("gradient", int(self.__state["gradient"].get())),
            ("dft", int(self.__state["dft"].get())),
            ("dct", int(self.__state["dct"].get())),
        ]
        L = int(self.__state["train_count"].get())

        print("PARAMS: ")
        print(self.__state["database"].get())
        print(params)
        print(L)

        scores = parallel_recognition(db_name=self.__state["database"].get(), params=params, templ_to=L)

        print(scores)

        posx = 250
        posy = 250

        image = Image.open(path.join(DATA_PATH, "results", "parallel_experiment_result.png"))

        image = image.resize((500, 300))
        image = ImageTk.PhotoImage(image)
        self.__state["result_images"].append(image)
        self.canvas.create_image(posx, posy, image=image)

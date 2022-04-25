import random

from tkinter import RIGHT, VERTICAL, W, Y, Button, Canvas, Entry, Frame, Label, OptionMenu, Scrollbar, StringVar
from typing import Callable
from PIL import ImageTk, Image
from ...core.configuration import DATABASE_CONF
from ...core.features import features
from ...core.recognition import recognition


class ConsistentFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__state = {
            "database": StringVar(self, list(DATABASE_CONF.keys())[0]),
            "method": StringVar(self, list(features.keys())[0]),
            "parameter": StringVar(),
            "from": StringVar(),
            "to": StringVar(),
            "accuracy": StringVar(),
            "templates": [],
            "result_images": [],
        }

        self.tools_frame = Frame(self)
        self.canvas_frame = Frame(self)
        self.scroll_frame = Frame(self)

        self.canvas = Canvas(self.canvas_frame, width=600, height=1000, bg="#CACACA")

        self.vbar = Scrollbar(self.scroll_frame, orient=VERTICAL)
        self.vbar.config(command=self.canvas.yview)

        
        self.canvas.config(yscrollcommand=self.vbar.set)

        self.tools_frame.grid(column="0", row="0", sticky=W)
        self.canvas_frame.grid(column="1", row="0", sticky=W)
        self.scroll_frame.grid(column="2", row="0", sticky=W)

        self.database_dropdown()
        self.method_dropdown()
        self.parameter_entry()
        self.from_entry()
        self.to_entry()
        self.run_button()
        self.accuracy_label()
        self.canvas.pack()
        self.vbar.pack(side=RIGHT,fill=Y)

    def database_dropdown(self) -> None:
        self.__dropdown(
            self.tools_frame,
            "Database",
            self.__state["database"],
            list(DATABASE_CONF.keys()),
        )

    def method_dropdown(self) -> None:
        self.__dropdown(self.tools_frame, "Method", self.__state["method"], list(features.keys()))

    def parameter_entry(self) -> None:
        self.__entry(self.tools_frame, "Parameter", self.__state["parameter"])

    def from_entry(self) -> None:
        self.__entry(self.tools_frame, "From", self.__state["from"], "1")

    def to_entry(self) -> None:
        self.__entry(self.tools_frame, "To", self.__state["to"], "8")

    def run_button(self) -> None:
        self.__button(self.tools_frame, self.run_consistent, "Run Recognition")

    def accuracy_label(self) -> None:
        self.__accuracy_label = Label(self.tools_frame, text=f"")
        self.__accuracy_label.pack()

    def run_consistent(self):
        accuracy, images, templates = recognition(
            self.__state["database"].get(),
            self.__state["method"].get(),
            int(self.__state["parameter"].get()),
            int(self.__state["from"].get()),
            int(self.__state["to"].get()),
        )

        self.__state["accuracy"].set(accuracy)
        self.__accuracy_label.config(text=f'Accuracy: {self.__state["accuracy"].get()}')

        if accuracy == 0:
            return

        templ_posx = 50
        templ_posy = 50

        res_posx = 300
        res_posy = 50

        # random_indices = [random.randrange(len(images)) for _ in range(int(self.__state["to"].get()))]

        for index in range(len(list(images))):
            templ = Image.fromarray(templates[index])
            templ.resize((50, 80))
            templ = ImageTk.PhotoImage(templ)
            self.__state["templates"].append(templ)
            self.canvas.create_image(templ_posx, templ_posy, image=templ)

            templ_posy += 120

            img = Image.fromarray(images[index])
            img.resize((50, 80))
            img = ImageTk.PhotoImage(img)
            self.__state["result_images"].append(img)
            self.canvas.create_image(res_posx, res_posy, image=img)

            res_posy += 120

    def __dropdown(self, frame: Frame, label: str, var: StringVar, options: list) -> None:
        Label(frame, text=label).pack()
        OptionMenu(frame, var, *options).pack()

    def __entry(self, frame: Frame, label: str, var: StringVar, default: str = "") -> None:
        Label(frame, text=label).pack()
        entry = Entry(frame, textvariable=var)
        entry.insert(-1, default)
        entry.pack()

    def __button(self, frame: Frame, command: Callable, title="button", width=None, height=None) -> None:
        Button(frame, text=title, width=width, height=height, command=command).pack()

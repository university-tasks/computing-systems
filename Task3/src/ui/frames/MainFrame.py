from collections import Counter
from tkinter import W, Button, Canvas, Frame, Label, StringVar, filedialog
from typing import Callable
from PIL import Image, ImageTk
import cv2

from ...core.recognition.train import train
from ...core.recognition.recognition import recognition


class MainFrame(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.state = {
            "image": StringVar(),
        }

        self.tools_frame = Frame(self)
        self.canvas_frame = Frame(self)

        self.mark_label = Label(self.tools_frame, text="Style: ", font="20")

        self.canvas = Canvas(self.canvas_frame, width=1000, height=1000, bg="#AAAAAA")

        self.tools_frame.grid(column="0", row="0", sticky=W)
        self.canvas_frame.grid(column="1", row="0", sticky=W)

        

        self.result = []

        self.run_train_button()
        self.select_image_button()
        self.run_recognition_button()
        self.mark_label.pack()
        self.canvas.pack()


    def select_image_button(self) -> None:
        self.__button(self.tools_frame, self.select_image, "Select Painting")

    def run_train_button(self) -> None:
        self.__button(self.tools_frame, train, "Train")

    def run_recognition_button(self) -> None:
        self.__button(self.tools_frame, self.run_recognition, "Run Recognition")

    def run_recognition(self) -> None:

        self.canvas.delete("all")

        if self.state["image"].get() is None:
            raise Exception("Image not uploaded")

        image = cv2.imread(self.state["image"].get())
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        marks, desc_images = recognition([image])

        res_posx = 300
        res_posy = 150

        self.mark_label.config(text=f"Style: {Counter(marks.values()).most_common(1)[0][0]}")


        # for image in desc_images:
        for index, (method, marks) in enumerate(marks.items()):
            desc = Image.open(desc_images[index])
            desc = desc.resize((270, 270))
            desc = ImageTk.PhotoImage(desc)
            self.result.append(desc)
            self.canvas.create_image(res_posx, res_posy, image=desc)
            res_posy += 150
            self.canvas.create_text(res_posx, res_posy, text=f"{method} – {marks}")
            res_posy += 150

    
    def select_image(self) -> None:
        self.__filedialog("Select Painting", self.state["image"])

    def __filedialog(self, label:str , var: StringVar) -> None:
        var.set(filedialog.askopenfilename(title=label))

    def __button(self, frame: Frame, command: Callable, title="button", width=None, height=None) -> None:
        Button(frame, text=title, width=width, height=height, command=command).pack()
    
from .app import App
from .frames.ConsistentFrame import ConsistentFrame


class Consistent(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_frame = ConsistentFrame()
        self.main_frame.pack()

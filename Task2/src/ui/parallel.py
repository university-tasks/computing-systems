from .frames.ParallelFrame import ParallelFrame
from .app import App


class Parallel(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_frame = ParallelFrame()
        self.main_frame.pack()

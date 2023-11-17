class FrameManager:
    """
    this class manages the frame switching

    Attributes:
        frames(dict): a dictonary with frame name as key and frame object as
            value

        args(frame object): frame objects which the frame manager should switch
            between

    """
    def __init__(self, *args):
        self.frames = {}

        for frame in args: # making a key value pair
            self.frames[frame.frame_name] = frame

    def switch_frame(self, frame_name):
        """
        this method switches the frame

        arg:
            frame_name(str): frame name to switch to

        """
        self.frames[frame_name].show()

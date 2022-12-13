
class CenterWidgetMixin:
    def __init__(self) -> None:
        pass
    
    def center(self):
        self.update()
        appWidth = self.winfo_width()
        appHeight = self.winfo_height()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        X = int(screenWidth / 2 - appWidth / 2)
        Y = int(screenHeight / 2 - appHeight / 2)
        self.geometry(f'{appWidth}x{appHeight}+{X}+{Y}')
    
    
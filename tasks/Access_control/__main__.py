from tkinter import Tk
from src.ent.database import DBContext
from src.controller.controler import MainController
from typing import Union



class App(Tk):
    db = DBContext()
    
    def __init__(self, screenName: Union[str, None] = None, baseName: Union[str, None] = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: Union[str, None] = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self._build()
        self.current_frame = None

    
    def _build(self):
        MainController(self, App.db)


def main():
    window_width = 800
    window_height = 800
    
    app = App()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    
    app.title("Access Control")
    app.geometry("500x400")
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    app.resizable(False, False)
    app.geometry(f"{window_width}x{window_height}+{x}+{y}")
    app.mainloop()

if __name__=="__main__":
    main()

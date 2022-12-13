import menu
import sys
from ui import MainWindow


if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) == 1:
        menu.start()
    elif len(args) == 2 or args[2] == '--ui':
        app = MainWindow()
        app.mainloop()
    
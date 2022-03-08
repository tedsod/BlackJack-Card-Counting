import tkinter as tk
from gui import gui

def main():
    root = tk.Tk()
    new_gui = gui.MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
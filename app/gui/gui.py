import tkinter as tk
from tkinter import StringVar, ttk

from pyparsing import col
from setuptools import setup
from sqlalchemy import column


class MainWindow():
    def __init__(self, parent):
        self.root = parent

        for index in [0, 1, 2]:
            self.root.columnconfigure(index=index, weight=1)
            self.root.rowconfigure(index=index, weight=1)

        self.root.title("BlackJack simulaiton")

        self.st = ttk.Style()
        self.root.tk.call("source", "app/resources/Sun-Valley-ttk-theme-master/sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")

        #Create variables

        self.setup_buttons()

    def setup_buttons(self):
        self.btn_frame = ttk.LabelFrame(self.root, padding="10 10 20 10")
        self.btn_frame.grid(column=1, row=0, sticky="NEWS")

        ttk.Label(self.btn_frame, text="Insert Money").grid(column=1, row=1, padx=5, sticky="w")
        ttk.Label(self.btn_frame, text="Bet Amount").grid(column=1, row=2, padx=5, sticky="w")


        entry_money = ttk.Entry(self.btn_frame, width=15).grid(row=1, column=2)
        entry_bet = ttk.Entry(self.btn_frame, width=15).grid(row=2, column=2)


    
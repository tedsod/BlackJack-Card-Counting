import sys 
sys.path.insert(1, 'BlackJack_project/src')
from main import main_loop
import tkinter as tk
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from scipy.stats import norm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

df_money = {}



class App:
    def __init__(self, root):
        self.root = root

# Just simply import the azure.tcl file
        root.tk.call("source", "BlackJack_Project/src/gui/azure.tcl")

        # Then set the theme you want with the set_theme procedure
        root.tk.call("set_theme", "light.tcl")
        btn = Button(root, text="Start", command=lambda: main_loop(10, 1))
        btn.place(x=370, y=550)

        lbl = Label(root, text="Betting Strategy", font=("Arvo", 14))
        #lbl.place(x=250, y=150)
        lbl.place(x=40, y=70)

        var = StringVar()
        var.set("one")
        data = ("Kelly Criterion", "Throp", "bet1", "bet2", "constant")
        cb = Combobox(root, values=data, text="Betting Strategy")
        #cb.place(x=6, y=150)
        cb.place(x=40, y=100)

        entry1 = Entry(root, width=21)
        entry1.place(x=40, y=150)

        lbl = Label(root, text="Input Money", font=("Arvo", 14))
        #lbl.place(x=250, y=150)
        lbl.place(x=40, y=125)

        Deck_nr = IntVar()
        Deck_nr2 = IntVar()
        Deck_nr3 = IntVar()
        Checkbutton(root, text="2", variable=Deck_nr).place(x=40, y=240)
        Checkbutton(root, text="4", variable=Deck_nr2).place(x=40, y=270)
        Checkbutton(root, text="6", variable=Deck_nr3).place(x=40, y=300)

        btn2 = Button(root, text="confirm", command=lambda: ())
        btn2.place(x=270, y=97)


        root.title('Blackjack')
        root.geometry('800x600')

        # creating a lable widget
        #myLabel1 = Label(root, text='Blackjack').grid(row=0, column=0)
        #myLabel2 = Label(root, text='Blackjack counting cards').grid(row=1, column=0)
        fig = Figure(figsize = ([0, 0]),
                        dpi = 200)

        plot1 = fig.add_subplot(111)
        fig, ax = plt.subplots()
        sns.lineplot(data=df_money,
        x='xaxis',
        y='money_change',
        ax=ax)
        plt.xlabel('Games played')
        plt.ylabel('Money')
        plt.title('Betting with units in regard to current bankroll')
        ax2 = plt.axes([0.25, 0.55, .2, .2], facecolor='lightgrey')
        sns.lineplot(data=df_money,
        x='xaxis',
        y='money_change',
        ax=ax2)
        ax2.set_title('zoom')
        ax2.set_xlim([0,5000])
        ax2.set_ylim([9500,11000])

        canvas = FigureCanvasTkAgg(fig, master = root)  
        canvas.draw()
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().place(x=300, y=40)

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        ##canvas.get_tk_widget().pack()



root = Tk()
my_gui = App(root)
my_gui.mainloop()

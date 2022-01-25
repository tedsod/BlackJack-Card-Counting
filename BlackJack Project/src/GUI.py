from tkinter import *
from tkinter.ttk import Combobox





#import counting
def btn_cmd():
    print("test")
    return None

def btn2_cmd():
    text = entry1.get()
    print(text)

root = Tk()
btn = Button(root, text="Start", command=btn_cmd)
#btn.place(x=400,y=350)
btn.pack()

lbl=Label(root, text="Betting Strategy", font=("Arvo", 14))
#lbl.place(x=250, y=150)
lbl.pack()

var= StringVar()
var.set("one")
data=("Kelly Criterion", "Throp", "bet1", "bet2", "constant")
cb = Combobox(root, values=data)
#cb.place(x=6, y=150)
cb.pack()

entry1 = Entry(root, width = 40)
entry1.pack()
btn2 = Button(root, text="confirm", command=btn2_cmd)
btn2.pack()


root.title('Blackjack')
root.geometry('800x600')

#creating a lable widget
#myLabel1 = Label(root, text='Blackjack').grid(row=0, column=0)
#myLabel2 = Label(root, text='Blackjack counting cards').grid(row=1, column=0)




root.mainloop()


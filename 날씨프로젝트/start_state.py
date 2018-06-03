import game_framework
import Main
from tkinter import *

name = "StartState"

def enter():
    pass

def update():
    pass

def exit():
    window.destroy()
    pass

def process_next():
    game_framework.change_state(Main)

def run():
    global window
    window = Tk()
    window.title('기상정보 알리미')
    window.geometry('500x500')  # width x height + 가로격자+세로격자

    map = 'weather.jpg'
    img = PhotoImage(file=map)

    map_label = Label(window, image=img)
    map_label.pack()
    button1 = Button(window,text="시작",command = process_next)
    button1.place(x=250,y=450)

    window.mainloop()





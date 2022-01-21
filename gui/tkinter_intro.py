from tkinter import *
from turtle import width

from click import command
window = Tk()
window.title('GUI Program')
window.minsize(width =500,height=500)
my_label =  Label(text = 'my label', font=('Arial', 24))
my_label.pack()

my_label['text'] = 'New text'

button_click = 0
def button_clicked():
    global button_click
    button_click += 1
    # my_label['text'] = f'Clicked: {button_click} times'
    new_txt = input.get()
    my_label['text'] = new_txt

input = Entry(width = 10)
input.pack()
button = Button(text='click me',  command=button_clicked)
button.pack()


window.mainloop()
